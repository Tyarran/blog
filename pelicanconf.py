# -*- coding: utf-8 -*-
AUTHOR = u'Romain Commandé'
SITENAME = u"Romain Commandé"
SITEURL = 'http://www.rcmd.tech'
TIMEZONE = "Europe/Paris"

GITHUB_URL = 'http://github.com/rcommande/'
DISQUS_SITENAME = "unblogsurlabanquise"
GOOGLE_ANALYTICS = "UA-31092671-1"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 6
DEFAULT_DATE_FORMAT = '%A %e %B %Y'
DEFAULT_CATEGORY = 'Général'
DEFAULT_LANG = 'fr'
SITESUBTITLE = "Romain Commandé, Développeur passionné d'impression 3D"
SITELOGO = "/images/profile.png"
MAIN_MENU = True

# PATH = '.'
ARTICLE_PATHS = ['articles']

FEED_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
ARTICLE_URL = '{slug}.html'
TAG_URL = 'tag/{slug}.html'
# PAGE_DIR = 'billets/pages'
PAGE_URL = 'pages/{slug}.html'
# REVERSE_CATEGORY_ORDER = True

LINKS = (
    # ('Planet Libre', 'http://planet-libre.org'),
    # ('Reflets', 'http://reflets.info'),
    # ('noirbizarre', 'http://www.noirbizarre.info'),
    # ('sam et max', 'http://www.sametmax.com'),
)


SOCIAL = (('twitter', 'http://twitter.com/rcommande'),
          # ('lastfm', 'https://www.last.fm/fr/user/minimumserious'),
          # ('bitbucket', 'http://bitbucket.org/minimumserious'),
          ('linkedin', 'https://www.linkedin.com/in/commanderomain/'),
          ('instagram', 'https://www.instagram.com/rcommande/'),
          ('github', 'http://github.com/rcommande'),
          ('rss', 'https://rcmd.tech/feeds/all.atom.xml'),)

DISPLAY_CATEGORIES_ON_MENU = True


# TEMPLATE_PAGES = {'../pages/archives.html': 'pages/archives.html'}

# global metadata to all the contents
DEFAULT_METADATA = (('', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["pictures", "images"]

# A list of files to copy from the source to the destination
# FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

# THEME = 'tuxlite_tbs'
THEME = '/home/romain/pelican-themes/Flex/'
# THEME = '/home/romain/pelican-themes/hyde/'

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"

RELATIVE_URLS = True
# PLUGINS = ['i18n_subsites']
# JINJA_ENVIRONMENT = ['jinja2.ext.i18n']
# DEFAULT_LANG = 'fr'
# LOCALE = "fr_FR.UTF-8"

# Translate to German.
DEFAULT_LANG = 'fr'
# OG_LOCALE = 'fr_FR'
# LOCALE = 'fr_FR'

LOCALE = ('en_US.utf8', 'fr_FR.utf8',)

# Default theme language.
I18N_TEMPLATES_LANG = 'fr_FR'


MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

