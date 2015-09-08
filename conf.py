# -*- coding: utf-8 -*-
AUTHOR = u'Romain Commandé'
SITENAME = u"Romain Commandé"
SITEURL = 'http://www.rcomman.de'
TIMEZONE = "Europe/Paris"

GITHUB_URL = 'http://github.com/rcommande/'
DISQUS_SITENAME = "unblogsurlabanquise"
GOOGLE_ANALYTICS = "UA-31092671-1"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "fr_FR.UTF-8"
DEFAULT_PAGINATION = 6
DEFAULT_DATE_FORMAT = '%A %e %B %Y'
DEFAULT_CATEGORY = 'Général'
DEFAULT_LANG = 'fr'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
ARTICLE_URL = '{slug}.html'
TAG_URL = 'tag/{slug}.html'
# PAGE_DIR = 'billets/pages'
PAGE_URL = 'pages/{slug}.html'
# REVERSE_CATEGORY_ORDER = True

LINKS = (
    ('Planet Libre', 'http://planet-libre.org'),
    ('Reflets', 'http://reflets.info'),
    ('noirbizarre', 'http://www.noirbizarre.info'),
    ('sam et max', 'http://www.sametmax.com'),
)


SOCIAL = (('twitter', 'http://twitter.com/rcommande'),
          ('lastfm', 'http://lastfm.com/user/minmumserious'),
          ('bitbucket', 'http://bitbucket.org/minimumserious'),)


# TEMPLATE_PAGES = {'../pages/archives.html': 'pages/archives.html'}

# global metadata to all the contents
DEFAULT_METADATA = (('', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["pictures", ]

# A list of files to copy from the source to the destination
# FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

# THEME = 'tuxlite_tbs'
THEME = 'Colourise11'

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"

RELATIVE_URLS = True
