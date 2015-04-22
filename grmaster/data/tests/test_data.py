# -*- coding: utf-8 -*-

"""Tests for standard test tables."""

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

from os.path import join, basename

from grmaster import data
from grmaster.table import Table
from glob import iglob

def test_load():
    """Test if wrong data folder."""
    table = data.load('students.csv')
    assert isinstance(table, Table)
    assert len(table) > 0

def test_streams_info():
    """Test that every file have streams_info."""
    for filename in iglob(join(data.DATA_DIR, '*.csv')):
        assert data.get_streams_info(basename(filename)) is not None
