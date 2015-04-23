#!/bin/env python3
# -*- coding: utf-8 -*-

# TODO: add link to doc.

"""
group-master - tool for dividing students into groups
Copyright (C) 2015  Lutov V. S. <vslutov@yandex.ru>

Don't panic! Just follow the instruction.
If you have a problem, read the doc: #link.
If you have read the doc, but problem are staying, please, write me a letter.
"""

#   group-master - tool for dividing students into groups
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

# from grmaster import Manager

import sys
from grmaster import Manager, data, rules

USAGE = """
Usage: {0} COMMAND

Available commands:
  --help            Show this help and exit
  --license         Show license and exit
  --template        Print csv template on stdout
  --divide file     Run dividing process""".format(sys.argv[0])

def printfile(filename):
    """Load file from data folder and print it."""
    file = data.openfile(filename)
    txt = file.readlines()
    file.close()
    sys.stdout.writelines(txt)


def main():
    """Print usage and exec simple commands."""
    if len(sys.argv) == 2 and sys.argv[1] == '--license':
        printfile('LICENSE.txt')
    elif len(sys.argv) == 2 and sys.argv[1] == '--template':
        printfile('template.csv')
    elif len(sys.argv) == 3 and sys.argv[1] == '--divide':
        input_file = open(sys.argv[2], 'r')
        manager = Manager(input_file)
        input_file.close()
        rules.english_rule(manager)
        print(manager.students.to_csv())
    else:
        print(USAGE)

if __name__ == '__main__':
    main()
