#!/usr/bin/env python
#This file is part of html2plaintext. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='html2plaintext',
        version='0.0.1',
        author='Zikzakmedia SL',
        author_email='zikzak@zikzakmedia.com',
        url="http://www.zikzakmedia.com/",
        description="Python module to convert HTML to Plain Text",
        long_description=read('README'),
        download_url="https://bitbucket.org/zikzakmedia/python-html2plaintext",
        packages=find_packages(),
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Office/Business :: Financial :: Accounting',
            'Topic :: Software Development :: Internationalization',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
        license='GPL-3',
        extras_require={
        },
        install_requires=['BeautifulSoup >= 3.2.1'],
        test_suite="html2plaintext.tests",
    )
