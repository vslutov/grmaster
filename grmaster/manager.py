# -*- coding: utf-8 -*-

"""Intermediate form of information about students and groups."""

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
from .stream import Stream


class Manager:

    """
    Manager is a list of streams.

    Manager() can be invoked with filename or Table argument.
    """

    streams = []

    def __init__(self, student_table):
        """Initialize self.  See help(type(self)) for accurate signature."""
        if isinstance(student_table, Table):
            self.students = student_table
        else:
            self.students = Table.from_csv_file(student_table)

    def setup_streams(self, streams_info):
        """Set up stream size info."""
        if self.streams == []:
            self.streams = []
            for stream_info in streams_info:
                self.streams.append(Stream(set() for i in range(stream_info)))
        else:
            raise TypeError('Streams have already set up')

    def get_assigned(self):
        """Get set of all assigned students."""
        result = set()
        for stream in self.streams:
            result |= stream.get_assigned()
        return result

    def get_assigned_count(self):
        """Return count of assigned students."""
        return len(self.get_assigned())

    def is_assigned(self, student):
        """Return True, if student is assigned to some stream."""
        return any(student in stream for stream in self.streams)
