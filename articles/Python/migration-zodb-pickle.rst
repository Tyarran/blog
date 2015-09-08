Migration de données avec la ZODB et Pickle
###########################################
:date: 2015-06-08
:tags: Programmation, Développement, Python, ZODB, Pickle, Migrations
:Status: draft


Chose promise, chose due ! Voici mon billet sur la migration de données avec la ZODB et, de façon plus générique, Pickle. Sur le papier, utiliser le module Pickle pour stoquer des données de façon persistente a tout pour plaire. On peut sérialiser à peut prêt n'importe quel objet Python immediatement, et, pour ceux qui ne peuvent pas être sérialiser, il suffit d'implémenter les méthodes __getstate__()  et __setstate__(). Une fois que tout est en place, l'usage semble presque magique. Pour info, les exemples sont réalisés avec Python 3 (3.4 dans mon cas) :

.. code-block:: pycon

    >>> import datetime
    >>> import pickle
    >>> now = datetime.datetime.now()
    >>> serialized = pickle.dumps(now)

    # La variable "serialized" contient maintenant une chaine de caractère avec le contenu de la variable "now" sérialisé:
    >>> type(serialized)
    bytes
    >>> serialized
    b'\x80\x03cdatetime\ndatetime\nq\x00C\n\x07\xdf\x06\x08\t%\x15\t[\xc6q\x01\x85q\x02Rq\x03.'

    # Pour la restauration, c'est pas plus compliqué
    >>> result = pickle.loads(serialized)
    datetime.datetime(2015, 6, 8, 9, 37, 21, 613318)

Pour un usage simple, il n'y a pas grand chose de plus à savoir . En voyant cela, on se dit tout de suite que c'est génial, et que l'on va pouvoir refaire le monde avec Pickle. C'est presque vrai ! À l'usage, c'est un vrai bonheur que d'utiliser Pickle pour sérialiser/désérialiser ces données. C'est très simple et plutôt performant.

Mais, car il y a un gros "mais", on n'oublie un point très important: la migration de données. Dans l'exemple précédent, j'utilise un type "de base" (datetime.datetime) qui n'a que peut de chance de véritablement changer dans le temps. Mais que ce passe t'il si j'avais sérialisé mes propres objets métiers, et que, suite à diverse évolutions de mon application, je suis ammené à modifier mon model ?

.. code-block:: pycon

    >>> import pickle

    # On définit une class qui prend en compte un prénom et un nom
    >>> class User(object):
    ...     def __init__(self, firstname, lastname):
    ...         self.firstname = firstname
    ...         self.lastname = lastname
    ...
    ...     def introduce(self):
    ...         print("{} {}".format(self.firstname, self.lastname)
    ...

    # On instancie un object User, on joue avec et on le sérialise avec Pickle
    >>> user = User('Romain', 'Commandé')
    >>> user.introduce()
    Romain Commandé
    >>> serialized_user = pickle.dumps(user)

    # Notre application évolue et notre class User ne correspond plus au besoin
    >>> class User(object):
    ...     def __init__(self, name):
    ...         self.name = name
    ...
    ...     def introduce(self):
    ...         print("{}".format(self.name)
    ...

    # Que ce passe-t'il si je désérialise mon objet ?
    >>> deserialized_user = pickle.loads(serialized_user)

    # Ça semble fonctionner, mais dans les faits, ça n'est pas vraiment le cas, les attributs de l'objet ne correspondent pas à ce que manipule la classe:
    >>> deserialized_user.introduce()
    AttributeError: 'User' object has no attribute 'name'

    # Maintenant que ce passe-t'il si la classe est supprimée ?
    >>> del User
    >>> deserialized_user = pickle.loads(serialized_user)
    AttributeError: Can't get attribute 'User' on <module '__main__'>

    # C'est pire, on ne peut même plus désérialiser notre objet. Le résultat aurait été le même si la classe avait juste été déplacée. C'est marqué noir sur blanc dans la doc officielle de Python, pickle peut désérialiser à peut prêt n'importe quoi a condition qu'il retrouve bien la classe de l'objet au moment endroits que lors de la sérialisation

    # Un dernier cas encore plus tordu avec des méthodes __setstate__ incompatibles:
    >>> class User(object):
    ...     def __init__(self, name):
    ...         self.name = name
    ...
    ...     def introduce(self):
    ...         print("{}".format(self.name)
    ...
    ...     def __setstate__(self, arg1, arg2):
    ...         pass  # just an example
    ...

    >>> deserialized_user = pickle.loads(serialized_user)
    TypeError: __setstate__() missing 1 required positional argument: 'args2'

    # Dans la pratique, je ne penses pas que ce cas soit fréquent, mais je l'ai rencontré lors d'un refactoring où le MRO de la classe d'origine à complètement changé.

Résolution par monkey patching
------------------------------

Bon on se retrouve maintenant dans le cas où on a bien une classe User mais ils nous ai impossible de désérialiser l'objet. Alors comment faire ? Une des solutons possible, c'est de conserver un snapshot de l'ancien object et de monkey patcher notre code de façon à ce que cette class soit disponible au bon endroit afin d'y appliquer une migration et obtenir un objet désérialisable par la nouvelle classe:

.. code-block:: pycon

    # On ajoute une nouvelle classe "OldUser" qui est un snapshot de l'ancienne classe "User"
    >>> class OldUser(object):
    ...     def __init__(self, firstname, lastname):
    ...         self.firstname = firstname
    ...         self.lastname = lastname
    ...
    ...     def introduce(self):
    ...         print("{} {}".format(self.firstname, self.lastname)
    ...

    >>> import sys
    # On stoke notre classe User ailleurs pour la retrouver plus tard
    >>> NewUser = User
    # Puis on remplacer User par OldUser
    >>> User = OldUser
