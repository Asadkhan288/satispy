#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import absolute_import
from setuptools import setup, Extension

cnfmodule = Extension(
    'satispy.cnf',
    sources = [
        'src/ext/cnf_module.c',
        'src/ext/cnf_cnf.c',
        'src/ext/cnf_variable.c',
        'src/ext/cnf_variableset.c'
    ]
)

setup(
    name='satispy',
    version='1.1b1',
    description='An interface to SAT solver tools (like minisat)',
    author='FÁBIÁN Tamás László',
    author_email='giganetom@gmail.com',
    url='https://github.com/netom/satispy/',
    download_url='https://github.com/netom/satispy/tarball/1.1b1#egg=satispy-1.1b1',
    license='BSD License',
    platforms='OS Independent',
    package_dir = {'': 'src/python'},
    packages=['satispy', 'satispy.io', 'satispy.solver'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries'
    ],
    ext_modules = [cnfmodule]
)
