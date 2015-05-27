# -*- coding: utf-8 -*-

"""Rules, which must be executing."""

#   grmaster - tool for dividing students into groups
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

from itertools import product
import random

from grmaster.table import Table
from sys import exit

def divide(elem_count, group_count):
    """Random divide elems into groups."""
    sizes = [len(elem_count) // group_count] * group_count
    prefix = len(elem_count) % group_count
    sizes[:prefix] = [len(elem_count) // group_count + 1] * prefix
    return sizes

def set_item(container, indeces, value):
    """Set item in recursive list."""
    while len(indeces) > 1:
        container = container[indeces[0]]
        indeces = indeces[1:]
    container[indeces[0]] = value

def get_item(container, indeces):
    """Get item from recursive list."""
    while len(indeces) > 1:
        container = container[indeces[0]]
        indeces = indeces[1:]
    return container[indeces[0]]

def init_meta_english_groups(manager):
    """Init meta for english rule."""
    header = manager.config['english_header'][0]
    index = manager.students.header.index(header)
    manager.meta['_english_index'] = index
    per_group = int(manager.config['english_per_group'][0])

    levels = manager.students.split_by_header(header)
    levels.sort(key=len)

    manager.meta['_english_groups'] = [[[''] * per_group
                                        for i in range(stream_size)]
                                       for stream_size in manager.stream_sizes]
    meta_english_groups = manager.meta['_english_groups']

    groups = [[(stream, group, half)
               for group in range(manager.stream_sizes[stream])
               for half in range(per_group)]
              for stream in range(len(manager.stream_sizes))]
    for stream in groups:
        random.shuffle(stream)

    group_count = sum(len(stream) for stream in groups)
    group_size = len(manager.students) // group_count

    # Every english level must have a group on each stream
    for level in levels:
        level_group_count = len(level) // group_size

        for stream in groups:
            if level_group_count <= 0:
                break
            else:
                group = stream[0]
                stream.remove(group)
                set_item(meta_english_groups, group, level[0][index])
                level_group_count -= 1

    groups = [group for stream in groups for group in stream]
    random.shuffle(groups)

    for level in levels:
        level_group_count = len(level) // group_size - len(manager.stream_sizes)

        if level_group_count > 0:
            for group in groups[:level_group_count]:
                groups.remove(group)
                set_item(meta_english_groups, group, level[0][index])

def english_rule(manager, student, group):
    """Test if student can study in group."""
    index = manager.meta['_english_index']
    return student[index] in get_item(manager.meta['_english_index'], group)

def add_english_rule(manager):
    """Add english rule for futher using."""
    init_meta_english_groups(manager)
    manager.rule_chain.append(english_rule)
