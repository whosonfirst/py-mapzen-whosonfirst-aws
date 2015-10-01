#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.aws',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.aws'],
    version='0.1',
    description='Tools and helper library for working with Amazon Web Services (AWS) and Who\'s on First data',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-aws',
    install_requires=[
        'boto',
        'geojson',
        'mapzen.whosonfirst.utils>=0.06',
        ],
    dependency_links=[
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-utils/tarball/master#egg=mapzen.whosonfirst.utils-0.06',
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/mapzen/py-mapzen-whosonfirst-aws/releases/tag/v0.1',
    license='BSD')
