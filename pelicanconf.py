#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'IAAR'
SITENAME = u'IAAR Capacitación'
SITESUBTITLE = u'Sitio de Capacitaciones de IAAR'
SITEURL = ''

#PATH = 'content'

TIMEZONE = 'America/Argentina/Buenos_Aires'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

STATIC_PATHS = ['favicon.ico']

# Set the article URL
ARTICLE_URL = 'capacitacion/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'capacitacion/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

MENUITEMS = [('IAAR', 'http://iaar.site/'),
             ('Home', '/index.html'),             
             ('Archives', '/archives.html')]

# Blogroll
LINKS = (('Relopezbriega', 'http://relopezbriega.github.io/'),
         ('Python.org', 'http://python.org/'),
         ('IAAR', 'http://iaar.site/'),
         ('IAAR Facebook', 'https://www.facebook.com/groups/InteligenciaArtificialArgentina/'),
         ('IAAR Meetup', 'https://www.meetup.com/es-ES/InteligenciaArtificialArgentina/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/IAARhub/'),)

DEFAULT_PAGINATION = 10

THEME = 'pelican-octopress-theme/'

DISPLAY_PAGES_ON_MENU = False

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#GITHUB_URL = 'https://github.com/blogen5minutos/blog_template'

if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
  EXTRA_HEADER = open('_nb_header.html').read()

# Sharing
#TWITTER_USER = 
#GOOGLE_PLUS_USER = 
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = True
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'


# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'


# Search
SEARCH_BOX = True
