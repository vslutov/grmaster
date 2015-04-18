# -*- coding: utf-8 -*-

"""
Test cases for utils.
"""

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

from __future__ import absolute_import, division, generators, nested_scopes
from __future__ import print_function, unicode_literals, with_statement

from pytest import raises

from grmaster.utils import Table

table_tuple = (('Name', 'Surname', 'City'),
               ('Alex', 'Brown', 'Moscow'),
               ('John', 'Smith', 'Moscow'),
               ('Ed', 'Wood', 'Hollywood'))

table_str = """| Name | Surname | City      |
------------------------------
| Alex | Brown   | Moscow    |
| John | Smith   | Moscow    |
| Ed   | Wood    | Hollywood |"""

table_partition = ((('Alex', 'Brown', 'Moscow'), ('John', 'Smith', 'Moscow')),
                   (('Ed', 'Wood', 'Hollywood'),))

def test_table_new():
    table = Table(table_tuple)
    assert(table.header == table_tuple[0])
    assert(table == table_tuple[1:])


def test_from_file(tmpdir):
    table_file = tmpdir.join('table.csv')
    table_file.write("Name,Surname,City\nAlex,Brown,Moscow\n" +
                     "John,Smith,Moscow\nEd,Wood,Hollywood")
    table = Table.from_file(str(table_file))
    assert(table.header == table_tuple[0])
    assert(table == table_tuple[1:])


class TestTable(object):
    def setup(self):
        self.table = Table(table_tuple)


class TestMagic(TestTable):
    def test_table_str(self):
        assert(str(self.table) == table_str)

    def test_table_repr(self):
        table_repr = 'Table(' + str(table_tuple) + ')'
        assert(repr(self.table) == table_repr)

    def test_table_immutable(self):
        with raises(TypeError):
            self.table[0] = self.table[1]


class TestMethods(TestTable):
    def test_table_split(self):
        partition = tuple(sorted(self.table.split_by_column(2)))
        assert(partition == table_partition)
        partition = tuple(sorted(self.table.split_by_header('City')))
        assert(partition == table_partition)
