# -*- coding: utf-8 -*-

"""
Basic group type.

It's not only academic group.
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


class Group(list):
    def __init__(self, arg=[]):
        if type(arg) is int:
            super(Group, self).__init__()
            self.max_size = arg
        else:
            super(Group, self).__init__(arg)
            self.max_size = len(self)
