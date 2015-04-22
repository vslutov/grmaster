# -*- coding: utf-8 -*-

"""Tests for `grmaster.Manager`."""

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
from grmaster import data
from grmaster.manager import Manager

STUDENTS_TABLE = data.load('students.csv')
STREAMS_INFO = data.get_streams_info('students.csv')

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

def test_manager_setup_streams():
    """Method setup_streams may be called only once."""
    manager = Manager(STUDENTS_TABLE)
    manager.setup_streams(STREAMS_INFO)
    assert len(manager.streams[0]) == 6
    assert len(manager.streams[1]) == 6
    assert len(manager.streams[2]) == 6
    stream_list = [list(stream) for stream in manager.streams]
    assert stream_list == [[set()] * 6] * 3
    with raises(TypeError):
        manager.setup_streams((6, 6, 7))


class TestManager:

    """Tests for grmaster.Manager."""

    manager = None

    def setup(self):
        """Just setup manager."""
        self.manager = Manager(STUDENTS_TABLE)
        self.manager.setup_streams(STREAMS_INFO)
        self.manager.streams[1][3] |= {1, 2, 3}

    def test_manager_is_assigned(self):
        """Constant method."""
        assert self.manager.is_assigned(1)
        assert self.manager.is_assigned(2)
        assert self.manager.is_assigned(3)
        assert not self.manager.is_assigned(4)
        assert not self.manager.is_assigned(5)

    def test_manager_get_assigned(self):
        """Return set."""
        assert isinstance(self.manager.get_assigned(), set)
        assert self.manager.get_assigned() == {1, 2, 3}
        self.manager.streams[1][4] |= {1, 2, 4}
        assert self.manager.get_assigned() == {1, 2, 3, 4}

    def test_manager_get_assigned_count(self):
        """Return size of set."""
        assert isinstance(self.manager.get_assigned_count(), int)
        assert self.manager.get_assigned_count() == 3
        self.manager.streams[1][4] |= {1, 2, 4}
        assert self.manager.get_assigned_count() == 4
