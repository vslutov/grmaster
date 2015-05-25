# -*- coding: utf-8 -*-

"""Http interface for group-master."""

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

from grmaster import data
from flask import Flask, request, Response

APP = Flask(__name__)
INDEX_HTML = ''.join(data.readlines('index.html'))
TEMPLATE_CSV = ''.join(data.readlines('template.csv'))

@APP.route('/')
def index():
    return INDEX_HTML

@APP.route('/template.csv')
def template():
    return Response(TEMPLATE_CSV, mimetype='text/csv')

@APP.route('/result.csv', methods=['POST'])
def result():
    print(request)
    return Response(TEMPLATE_CSV, mimetype='text/csv')

def run(port=8000, app=APP):
    """Run httpserver on selected port."""

    app.run(port=port)
