#!/usr/bin/env python

import os
import sys

from glob import glob

from setuptools import setup

import DistUtilsExtra.command.build_extra
import DistUtilsExtra.command.build_i18n
import DistUtilsExtra.command.clean_i18n

# to update i18n .mo files (and merge .pot file into .po files) run on Linux:
# ,,python setup.py build_i18n -m''

# silence pyflakes, __VERSION__ is properly assigned below...
__VERSION__ = '0.3'
for line in open('station-tweak', 'r').readlines():
    if (line.startswith('__VERSION__')):
        exec(line.strip())
PROGRAM_VERSION = __VERSION__


def datafilelist(installbase, sourcebase):
    datafileList = []
    for root, subFolders, files in os.walk(sourcebase):
        fileList = []
        for f in files:
            fileList.append(os.path.join(root, f))
        datafileList.append((root.replace(sourcebase, installbase), fileList))
    return datafileList

data_files = [
    ('{prefix}/share/man/man1'.format(prefix=sys.prefix), glob('data/*.1')),
    ('{prefix}/share/applications'.format(prefix=sys.prefix),
     ['data/station-tweak.desktop']),
    ('{prefix}/share/polkit/actions'.format(prefix=sys.prefix),
     ['data/org.mate.station-tweak.policy']),
    ('{prefix}/share/mate-panel/layouts'.format(prefix=sys.prefix),
     ['data/classy.layout',
      'data/element.layout',
      'data/netbook.layout',
      'data/purity.layout',
      'data/windowy.layout']),
    ('{prefix}/lib/station-tweak'.format(prefix=sys.prefix),
     ['data/station-tweak.ui',
      'util/mate-panel-backup'])
]
data_files.extend(datafilelist('{prefix}/share/locale'.format(prefix=sys.prefix
                                                              ), 'build/mo'))

cmdclass = {"build": DistUtilsExtra.command.build_extra.build_extra,
            "build_i18n": DistUtilsExtra.command.build_i18n.build_i18n,
            "clean": DistUtilsExtra.command.clean_i18n.clean_i18n}

setup(name="station-tweak",
      version=PROGRAM_VERSION,
      description="Station Tweak is a toolset to fine-tune the MATE desktop",
      license='GPLv2+',
      author='Eric Turgeon',
      url='https://github/GhostBSD/station-tweak/',
      package_dir={'': '.'},
      data_files=data_files,
      install_requires=['setuptools'],
      scripts=['station-tweak'],
      cmdclass=cmdclass)
