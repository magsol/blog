#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Shannon Quinn'

SITENAME = u'Stochastic Stenography'
SITETITLE = SITENAME
SITESUBTITLE = u'Data science, academia, and donuts'
SITELOGO = u'http://magsol.github.io/images/me.png'
SITEURL = 'http://127.0.0.1:8000'

# Times and dates.
TIMEZONE = u'America/New_York'
DEFAULT_LANG = u'en'
OG_LOCALE = u'en_US'
DEFAULT_DATE_FORMAT = '%B %d, %Y, at %H:%M:%S. It was %A.'

PATH = './content'
STATIC_PATHS = ['downloads', 'images', 'figures', 'notebooks']
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
COPYRIGHT_YEAR = 2016

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = False

# MENUITEMS = (())

# LINKS = (())

# Social widget
SOCIAL = (('envelope-o', 'mailto:magsol@gmail.com'),
          ('twitter', 'https://twitter.com/SpectralFilter'),
          ('github', 'https://github.com/magsol'),
          ('stack-overflow', 'http://stackoverflow.com/users/13604/magsol'),
          ('google', 'https://plus.google.com/+ShannonQuinnBBQ/'),
          ('linkedin', 'http://www.linkedin.com/in/shannonpquinn'))

DEFAULT_PAGINATION = False

# This header file is automatically generated by the notebook plugin
# if not os.path.exists('_nb_header.html'):
#     import warnings
#     warnings.warn("_nb_header.html not found.  "
#                   "Rerun make html to finalize build.")
# else:
#     EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Woo plugins!
# MD_EXTENSIONS = ['figureAltCaption', 'external.figureAltCaption']
NOTEBOOK_DIR = 'notebooks'
THEME = 'Flex/'
PLUGIN_PATHS = ['pelican-plugins']
GIT_FILETIME_FOLLOW = True
PLUGINS = ['liquid_tags.img', 'liquid_tags.video', 'summary',
          'liquid_tags.include_code', 'liquid_tags.literal',
          'filetime_from_git', 'simple_footnotes']
# PLUGINS = ['liquid_tags.notebook'] -- doesn't like non-Octopress themes
# PLUGINS = ['figure-ref'] -- seems to hate on Markdown syntax
# PLUGINS = ['gallery'] -- don't need this just yet
# PLUGINS = ['tag_cloud'] -- requires heavy theme CSS modification


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
