#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.aws.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
version = open("VERSION").read()
desc = open("README.md").read()

setup(
    name='mapzen.whosonfirst.aws',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.aws'],
    version=version,
    description='Tools and helper library for working with Amazon Web Services (AWS) and Who\'s on First data',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-aws',
    install_requires=[
        'boto',
        'geojson',
        'mapzen.whosonfirst.utils>=0.18',
        ],
    dependency_links=[
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-utils/tarball/master#egg=mapzen.whosonfirst.utils-0.18',
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-aws/releases/tag/' + version,
    license='BSD')
