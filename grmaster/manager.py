# -*- coding: utf-8 -*-

"""
Intermediate form of information about students and groups.
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

from .table import Table


class Stream(list):
    """Stream is a list of groups."""

    def __repr__(self):
        return 'Stream(' + super().__repr__() + ')'

    def get_students(self):
        """Get set of all students."""
        result = set()
        for group in self:
            result |= group
        return result

    def get_student_count(self):
        """A part of student count."""
        return sum(len(group) for group in self)

class Manager:
    """Manager is a list of streams."""

    streams = None

    def __init__(self, student_table):
        if isinstance(student_table, Table):
            self.students = student_table
        else:
            self.students = Table.from_csv_file(student_table)

    def get_student_count(self):
        """Can run only after stream_info_step."""
        return sum(stream.get_student_count for stream in self.streams)

    # TODO: move to another file
    def english_rule(self, english_header):
        aggregates = self.students.split_by_header(english_header)
