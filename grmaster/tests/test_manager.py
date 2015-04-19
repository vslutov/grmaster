# -*- coding: utf-8 -*-

"""Tests for grmaster.manager."""

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
from grmaster import Manager
from grmaster import data

STUDENTS_TABLE = data.load('students.csv')

def test_manager_init(tmpdir):
    """Test if manager creates normally."""
    manager = Manager(STUDENTS_TABLE)
    assert isinstance(manager, Manager)
    assert manager.students == STUDENTS_TABLE

    table_file = tmpdir.join('table.csv')
    table_file.write(STUDENTS_TABLE.to_csv())
    manager = Manager(str(table_file))
    assert isinstance(manager, Manager)
    assert manager.students == STUDENTS_TABLE


class TestManager:

    """Tests for grmaster.manager."""

    manager = None

    def setup(self):
        """Just setup manager."""
        self.manager = Manager(STUDENTS_TABLE)

    def test_manager_setup_streams(self):
        """Method setup_streams may be called only once."""
        self.manager.setup_streams((6, 6, 6))
        assert len(self.manager.streams[0]) == 6
        assert len(self.manager.streams[1]) == 6
        assert len(self.manager.streams[2]) == 6
        stream_list = [list(stream) for stream in self.manager.streams]
        assert stream_list == [[set()] * 6] * 3
        with raises(TypeError):
            self.manager.setup_streams((6, 6, 7))
