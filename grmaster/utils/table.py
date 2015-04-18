# -*- coding: utf-8 -*-

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

import csv

class Table(object):
    """
    Immutable table with header.

    >>> users = Table((('Name', 'Surname', 'City'),
    ...                ('Alex', 'Brown', 'Moscow'),
    ...                ('Ed', 'Wood', 'Hollywood')))
    >>> users.header
    ('Name', 'Surname', 'City')
    >>> users[0]
    ('Alex', 'Brown', 'Moscow')
    """

    def __init__(self, table):
        table = tuple(tuple(row) for row in table)
        self.body = table[1:]
        self.header = table[0]

    def __str__(self):
        width = len(self.header)
        column_lens = [len(head) for head in self.header]

        for row in self:
            for i in range(width):
                column_lens[i] = max(column_lens[i], len(str(row[i])))

        def row_to_string(row):
            """Convert table row to string"""
            item = lambda i: str(row[i]).ljust(column_lens[i])
            return '| ' + ' | '.join(item(i) for i in range(width)) + ' |'

        header = row_to_string(self.header)
        body = '\n'.join(row_to_string(row) for row in self)
        return header + '\n' + '-' * len(header) + '\n' + body

    def __repr__(self):
        tuple_repr = repr((self.header,) + tuple(self))
        return type(self).__name__ + '(' + tuple_repr + ')'

    def __getitem__(self, key):
        if type(key) is int:
            return self.body[key]
        else: # type(key) is slice
            return type(self)((self.header,) + self.body[key])

    def split_by_column(self, index):
        cases = set(row[index] for row in self)
        return (tuple(filter(lambda row: row[index] == case,
                             self))
                for case in cases)

    def split_by_header(self, header):
        return self.split_by_column(self.header.index(header))

    def from_file(filename):
        input_file = open(filename, 'r')
        table = Table(csv.reader(input_file))
        input_file.close()
        return table
