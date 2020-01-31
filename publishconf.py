#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import logging
# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://dfrieds.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['extra',
                'python',
                'machine-learning',
                'data-visualizations',
                'data-analysis',
                'math',
                'teaching',
                'about',
                'articles'
                ]

# in content, we still have our folders
ARTICLE_URL = '{category}/{slug}.html'
PAGE_URL = '{slug}.html'

ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# https://docs.getpelican.com/en/stable/tips.html#copy-static-files-to-the-root-of-your-site
# https://stackoverflow.com/a/31270471/1710454
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
    }

ARTICLE_EXCLUDES = ['in_progress']
IGNORE_FILES = ['__pycache__', ".ipynb_checkpoints", '!./.ipynb_checkpoints/*']
# line below enables "metacell" - first cell in jupyter notebook - to have config details
IPYNB_USE_METACELL = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['pelican-plugins']
# pelican-ert is for estimating reading time
# render_math is for rendering math equations using latex
# ipynb.markup helps convert ipynb files to markdown for site generation
PLUGINS = ['sitemap', 'pelican-ert', 'render_math', 'pelican-ipynb.markup']

# reading time estimate plugin called pelican-ert
# wpm is words per minutes
ERT_WPM = 220
logging.debug("Use ERT_WPM: {0}".format(ERT_WPM))
ERT_FORMAT = '{time}' # we include the word read afterwards in our html
ERT_INT = True

DIRECT_TEMPLATES = ['index']

# all of these are empty strings because I don't want a new page for just categories, just authors, etc. 
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.5,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily'
    }
}




# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""