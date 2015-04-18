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

from pytest import raises

from grmaster.utils import Table

table_tuple = (('Name', 'Surname', 'City'),
               ('Alex', 'Brown', 'Moscow'),
               ('John', 'Smith', 'Moscow'),
               ('Эд', 'Wood', 'Hollywood')) # Testing unicode

table_str = """| Name | Surname | City      |
------------------------------
| Alex | Brown   | Moscow    |
| John | Smith   | Moscow    |
| Эд   | Wood    | Hollywood |"""

table_csv = """Name,Surname,City
Alex,Brown,Moscow
John,Smith,Moscow
Эд,Wood,Hollywood"""

table_partition = ((('Alex', 'Brown', 'Moscow'), ('John', 'Smith', 'Moscow')),
                   (('Эд', 'Wood', 'Hollywood'),))

def test_table_new():
    table = Table(table_tuple)
    assert(table.header == table_tuple[0])
    assert(tuple(table) == table_tuple[1:])


def test_from_csv_file(tmpdir):
    table_file = tmpdir.join('table.csv')
    table_file.write(table_csv)
    table = Table.from_csv_file(str(table_file))
    assert(table.header == table_tuple[0])
    assert(tuple(table) == table_tuple[1:])


def test_from_csv_str():
    table = Table.from_csv_str(table_csv)
    assert(table.header == table_tuple[0])
    assert(tuple(table) == table_tuple[1:])


class TestTable(object):
    def setup(self):
        self.table = Table(table_tuple)


class TestMagic(TestTable):
    def test_table_str(self):
        assert(str(self.table) == table_str)

    def test_table_slice(self):
        assert(type(self.table[:-1]) is Table)
        assert(tuple(self.table[:-1]) == table_tuple[1:-1])

    def test_table_repr(self):
        table_repr = 'Table(' + str(table_tuple) + ')'
        assert(repr(self.table) == table_repr)

    def test_table_immutable(self):
        with raises(TypeError):
            self.table[0] = self.table[1]

    def test_len(self):
        assert(len(self.table) == len(table_tuple) - 1)

    def test_eq(self):
        other = Table(table_tuple)
        assert(self.table == other)


class TestMethods(TestTable):
    def test_table_split(self):
        partition = tuple(sorted(self.table.split_by_column(2)))
        assert(partition == table_partition)
        partition = tuple(sorted(self.table.split_by_header('City')))
        assert(partition == table_partition)


    def test_table_to_csv(self):
        assert(self.table.to_csv() == table_csv)
