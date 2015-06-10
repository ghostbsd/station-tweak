#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2015 by Mike Gabriel <mike.gabriel@das-netzwerkteam.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA.

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
__VERSION__ = '0.0.0.0'
for line in file('station-tweak').readlines():
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
    ('{prefix}/share/applications'.format(prefix=sys.prefix), ['data/station-tweak.desktop',]),
    ('{prefix}/share/station-tweak'.format(prefix=sys.prefix), ['data/mate-volume-control-applet.desktop',]),
    ('{prefix}/share/polkit/actions'.format(prefix=sys.prefix), ['data/org.mate.station-tweak.policy',]),
    ('{prefix}/share/mate-panel/layouts'.format(prefix=sys.prefix), ['data/classic.layout', 'data/element.layout', 'data/purity.layout',]),
    ('{prefix}/lib/station-tweak'.format(prefix=sys.prefix), ['data/station-tweak.ui', 'util/disable-mate-volume-applet', 'util/mate-panel-backup']),
]
data_files.extend(datafilelist('{prefix}/share/locale'.format(prefix=sys.prefix), 'build/mo'))

cmdclass ={
            "build" : DistUtilsExtra.command.build_extra.build_extra,
            "build_i18n" :  DistUtilsExtra.command.build_i18n.build_i18n,
            "clean": DistUtilsExtra.command.clean_i18n.clean_i18n,
}

setup(
    name = "station-tweak",
    version = PROGRAM_VERSION,
    description = "Station Tweak is a toolset to fine-tune the MATE desktop environment",
    license = 'GPLv2+',
    author = 'Eric Turgeon',
    url = 'https://github/GhostBSD/station-tweak/',
    package_dir = {'': '.'},
    data_files = data_files,
    install_requires = [ 'setuptools', ],
    scripts = ['station-tweak'],
    cmdclass = cmdclass,
)
