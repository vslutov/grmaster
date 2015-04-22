# -*- coding: utf-8 -*-

"""Rules, which must be executing."""

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

from itertools import product
import random


def divide(elems, groups):
    """Random divide elems into groups."""
    elems = list(elems)
    random.shuffle(elems)

    sizes = [len(elems) // groups] * groups
    prefix = len(elems) % groups
    sizes[:prefix] = [len(elems) // groups + 1] * prefix
    begins = [sum(sizes[:i]) for i in range(groups)]
    return [set(elems[begins[i]:begins[i]+sizes[i]]) for i in range(groups)]

def english_rule(manager, english_header, per_group=2):
    """Forming groups with fixed english level."""
    if manager.streams == []:
        raise TypeError('You must specify stream info first.')

    english_levels = manager.students.split_by_header(english_header)
    english_levels.sort(key=len)

    streams = []
    for i in range(len(manager.streams)):
        stream = manager.streams[i]
        stream = list(product((i,), range(len(stream)), range(per_group)))
        streams += stream
    random.shuffle(streams)

    avail_groups = len(streams)
    students_per_group = len(manager.students) / avail_groups

    for i in range(len(english_levels)):
        level = english_levels[i]
        groups_on_level = round(len(level) / students_per_group)
        if i == len(english_levels) - 1:
            groups_on_level = avail_groups
        avail_groups -= groups_on_level

        for eng_group in divide(level, groups_on_level):
            study_group = streams.pop()
            manager.streams[study_group[0]][study_group[1]] |= eng_group
