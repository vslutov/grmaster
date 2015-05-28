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

from grmaster.manager import set_item, get_item
from sys import exit

def divide(elem_count, group_count):
    """Random divide elems into groups."""
    sizes = [elem_count // group_count] * group_count
    prefix = elem_count % group_count
    sizes[:prefix] = [elem_count // group_count + 1] * prefix
    print(elem_count, group_count)
    return sizes

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

    groups = [[group[0], group[1], i]
              for group in manager.group_ids
              for i in range(per_group)]
    random.shuffle(groups)

    group_count = len(groups)
    group_size = len(manager.students) // group_count

    for i in range(len(levels)):
        level_group_count = len(levels[i]) // group_size
        if level_group_count == 0:
            level_group_count = 1
        if i == len(levels) - 1:
            level_group_count = group_count
        else:
            group_count -= level_group_count

        for group, students in zip(groups,
                                   divide(len(levels[i]), level_group_count)):
            set_item(meta_english_groups, group, [levels[i][0][index], students])

        groups = groups[level_group_count:]

def english_rule(manager, student, group):
    """Test if student can study in group."""
    index = manager.meta['_english_index']
    for en_type, count in get_item(manager.meta['_english_groups'], group):
        if en_type == student[index] and count > 0:
            return True
    return False

def english_add(manager, student, group):
    """Try to add student to group."""
    index = manager.meta['_english_index']
    if manager.can_study(student, group):
        for en_box in get_item(manager.meta['_english_groups'], group):
            if en_box[0] == student[index] and en_box[1] > 0:
                en_box[1] -= 1
                return True
    return False

def add_english_rule(manager):
    """Add english rule for futher using."""
    init_meta_english_groups(manager)
    manager.rule_chain.append(english_rule)
    manager.add_chain.append(english_add)
