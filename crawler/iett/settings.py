# -*- coding: utf-8 -*-

# Scrapy settings for iett project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'iett'

SPIDER_MODULES = ['iett.spiders']
NEWSPIDER_MODULE = 'iett.spiders'

ITEM_PIPELINES = {
    'iett.pipelines.MultiCSVItemPipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'iett (+http://www.yourdomain.com)'

# ======= CRAWLERA SETTINGS =========
# Uncomment below and fill your CRAWLERA_USER with your API KEY.

# DOWNLOADER_MIDDLEWARES = {'scrapy_crawlera.CrawleraMiddleware': 600}
# CRAWLERA_ENABLED = True
# CRAWLERA_USER = ''
# CRAWLERA_PASS = ''

# CONCURRENT_REQUESTS = 32
# CONCURRENT_REQUESTS_PER_DOMAIN = 32
# AUTOTHROTTLE_ENABLED = False
# DOWNLOAD_TIMEOUT = 600
