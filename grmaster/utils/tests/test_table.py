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

TABLE_TUPLE = (('Name', 'Surname', 'City'),
               ('Alex', 'Brown', 'Moscow'),
               ('John', 'Smith', 'Moscow'),
               ('Эд', 'Wood', 'Hollywood'))  # Testing unicode

TABLE_STR = """| Name | Surname | City      |
------------------------------
| Alex | Brown   | Moscow    |
| John | Smith   | Moscow    |
| Эд   | Wood    | Hollywood |"""

TABLE_CSV = """Name,Surname,City
Alex,Brown,Moscow
John,Smith,Moscow
Эд,Wood,Hollywood"""

TABLE_PARTITION = ((('Alex', 'Brown', 'Moscow'), ('John', 'Smith', 'Moscow')),
                   (('Эд', 'Wood', 'Hollywood'),))


def test_table_new():
    table = Table(TABLE_TUPLE)
    assert table.header == TABLE_TUPLE[0]
    assert tuple(table) == TABLE_TUPLE[1:]


def test_from_csv_file(tmpdir):
    table_file = tmpdir.join('table.csv')
    table_file.write(TABLE_CSV)
    table = Table.from_csv_file(str(table_file))
    assert table.header == TABLE_TUPLE[0]
    assert tuple(table) == TABLE_TUPLE[1:]


def test_from_csv_str():
    table = Table.from_csv_str(TABLE_CSV)
    assert table.header == TABLE_TUPLE[0]
    assert tuple(table) == TABLE_TUPLE[1:]


class TestTable:
    table = None
    def setup(self):
        self.table = Table(TABLE_TUPLE)


class TestTableMagic(TestTable):
    def test_table_str(self):
        assert str(self.table) == TABLE_STR

    def test_table_slice(self):
        assert isinstance(self.table[:-1], Table)
        assert tuple(self.table[:-1]) == TABLE_TUPLE[1:-1]

    def test_table_repr(self):
        table_repr = 'Table(' + str(TABLE_TUPLE) + ')'
        assert repr(self.table) == table_repr

    def test_table_immutable(self):
        with raises(TypeError):
            self.table[0] = self.table[1]

    def test_len(self):
        assert len(self.table) == len(TABLE_TUPLE) - 1

    def test_eq(self):
        other = Table(TABLE_TUPLE)
        assert self.table == other


class TestTableMethods(TestTable):
    def test_table_split(self):
        partition = self.table.split_by_column(2)
        sorted_partition = tuple(sorted(tuple(group) for group in partition))
        assert isinstance(partition, tuple)
        assert isinstance(partition[0], Table)
        assert sorted_partition == TABLE_PARTITION
        partition = self.table.split_by_header('City')
        sorted_partition = tuple(sorted(tuple(group) for group in partition))
        assert sorted_partition == TABLE_PARTITION

    def test_table_to_csv(self):
        assert self.table.to_csv() == TABLE_CSV
