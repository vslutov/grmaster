# -*- coding: utf-8 -*-

"""
Models of groups, streams, partitions etc.
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

from .utils import Table

class Group(list):
    def __init__(self, arg=[]):
        if type(arg) is int:
            super(Group, self).__init__()
            self.max_size = arg
        else:
            super(Group, self).__init__(arg)
            self.max_size = len(self)

class Stream(list):
    def __init__(self, size):
        super(Stream, self).__init__(Group for i in range(size))
        self.size = size


class Streams(list):
    def __init__(self, stream_sizes):
        super(Streams, self).__init__(Stream(size) for size in stream_sizes)

    def get_size(self):
        return sum(len(group) for group in self)


class Partition(object):
    def __init__(self, student_table, stream_sizes):
        if type(student_table) is Table:
            self.students = student_table
        else:
            self.students = Table.from_file(student_table)
        self.total_groups = sum(stream_sizes)
        self.streams = Streams(stream_sizes)

    # TODO: move to another file
    def english_rule(self, english_header):
        aggregates = self.students.split_by_header(english_header)
