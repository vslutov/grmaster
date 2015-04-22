# -*- coding: utf-8 -*-

"""Standard test tables and other usefull stuff."""

#   group-master - tool for divide students into groups
#   Copyright (C) 2015  Lutov V. S. <vslutov@yandex.ru>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from grmaster.table import Table

DATA_DIR = os.path.abspath(os.path.dirname(__file__))

def load(filename):
    """Load file from test data dir by name."""
    return Table.from_csv_file(os.path.join(DATA_DIR, filename))

def get_streams_info(filename):
    """
    Every file in library have connected info.

    Available files:
    - students.csv
    """
    if filename == 'students.csv':
        return (6, 6, 6)
