# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name         = 'iett',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = iett.settings']},
    package_data = {'iett': ['resources/bus_lines.csv', 'resources/linelist.csv']},

)
