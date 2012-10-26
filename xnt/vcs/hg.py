#!/usr/bin/env python

#   Xnt -- A Wrapper Build Tool
#   Copyright (C) 2012  Kenny Ballou

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
from mercurial import hg
from mercurial import ui
from mercurial import commands

def hgclone(url, dest=None,rev=None,branch=None):
    commands.clone(
        ui=ui.ui(),
        source=url,
        dest=dest,
        opts={"-r":rev,
              "-b":branch})

def hgfetch(path, source='default'):
    repo = hg.repository(ui.ui(), path)
    commands.pull(repo.ui, repo, source)
    commands.update(repo.ui, repo)
