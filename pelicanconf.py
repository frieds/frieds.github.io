#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import logging

AUTHOR = 'Dan Friedman'
SITENAME = "Dan Friedman's Data & Programming Knowledge Base"
SITEURL = ''
THEME = 'theme'
PATH = 'content'
GITHUB_URL = 'https://github.com/frieds'
TWITTER_USERNAME = '_danfriedman'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs' # I think with this you don't need to specify a date on posts
DEFAULT_DATE_FORMAT = '%b %-m %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# do this only for testing locally so we reference our local stylesheet
RELATIVE_URLS = True

# BELOW ALL USED TO BE IN PUBLISH!!!

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
PLUGINS = ['sitemap', 'pelican-ert', "render_math", 'pelican-ipynb.markup']

# reading time estimate plugin called pelican-ert
# wpm is words per minutes
ERT_WPM = 350
logging.debug("Use ERT_WPM: {0}".format(ERT_WPM))
ERT_FORMAT = '{time}' # we inlcude the word read afterwards in our html
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