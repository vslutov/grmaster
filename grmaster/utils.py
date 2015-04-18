# -*- coding: utf-8 -*-

"""
Usefull utils for dividing.
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

import csv

class Table(object):
    def __init__(self, table):
        table = tuple(tuple(row) for row in table)
        self.headers = table[0]
        self.body = table[1:]

    def __len__(self):
        return len(self.body)

    def split_by_column(self, index):
        cases = set([student[index] for student in self.body])
        return [list(filter(lambda student: student[index] == case,
                            self.body))
                for case in cases]

    def split_by_header(self, header):
        print(header)
        return self.split_by_column(self.headers.index(header))

    def from_file(filename):
        input_file = open(filename, 'r')
        table = Table(csv.reader(input_file))
        input_file.close()
        return table
