#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

from setuptools import setup, find_packages

import conekta
version = str(conekta.__version__)

setup(
    name='conekta',
    version=version,
    author='Julian Ceballos',
    author_email='julian@lastroom.mx',
    url='http://github.com/julianceballos/conekta',
    description='Easy Conekta python wrapper',
    long_description=open('./README.txt', 'r').read(),
    download_url='http://github.com/julianceballos/conekta/tarball/master',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: MIT License',
        ],
    packages=find_packages(),
    install_requires=[
        'requests',
        'inspect',
        'simplejson'
    ],
    license='MIT License',
    keywords='conekta api',
    include_package_data=True,
    zip_safe=True,
)