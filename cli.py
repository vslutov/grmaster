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

import os
from grmaster import Manager, data

LICENSE_DIR = os.path.abspath(os.path.dirname(__file__))

def choice(question, variants=None, default=None):
    """Input string, until have right input."""
    if variants is None and default is None:
        raise RuntimeError('use `input` instead of `choice`')

    if variants is not None:
        question += ' (' + '|'.join(variants) + ')'
    if default is not None:
        question += ' [default=' + default + '] '

    answer = None
    try:
        while answer is None:
            user_input = input(question)
            user_len = len(user_input)
            if user_input == '' and default is not None:
                answer = default
            else:
                if variants is not None:
                    for var in variants:
                        if len(var) >= user_len and var[:user_len] == user_input:
                            if answer is None:
                                answer = var
                            else:
                                answer = None
                                break
                else:
                    answer = user_input
    except KeyboardInterrupt:
        print()
        answer = None
    except EOFError:
        print()
        answer = None

    return answer

def main():
    """CLI entry point."""
    license_txt = data.load('LICENSE.txt')

    print(__doc__)
    print("""Now you can type:
    - help : get some help
    - license : read the license
    - start : start working\nJust press `enter` for default command.""")
    while True:
        action = choice('What you would do?', ['help', 'license', 'start'], 'start')
        if action == None:
            return
        elif action == 'help':
            print('Read the doc: #link')  # TODO: enter doc link
        elif action == 'license':
            print(license_txt)
        elif action == 'start':
            manager = None
            have_csv = choice('Have you ready csv table with '
                              'information about students?', ['yes', 'no'])
            if have_csv == 'no':
                print('Now new template file willbe created.')
                template_filepath = choice('Type a filepath to template csv '
                                        'table:', None, 'template.csv')
                template_file = open(template_filepath)
                data.save_template(template_file)
                template_file.close()
            else:  # have_csv == 'yes'
                while manager is None:
                    filepath_table = choice('Type a filepath to student '
                                            'table:', None, 'students.csv')
                    try:
                        manager = Manager(filepath_table)
                    except FileNotFoundError:
                        print('File not found')
            return

if __name__ == "__main__":
    main()
