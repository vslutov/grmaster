# -*- coding: utf-8 -*-

"""Http interface for grmaster."""

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

from grmaster import data, rules, Manager, setting
from flask import Flask, request, Response, abort
import tempfile

APP = Flask(__name__)
INDEX_HTML = data.readbytes('index.' + setting.LANG + '.html')
TEMPLATE_CSV = data.readbytes('template.csv')

@APP.route('/')
def index():
    """Language-specific function."""
    return INDEX_HTML

@APP.route('/template.csv')
def template():
    """One request, one template."""
    return Response(TEMPLATE_CSV, mimetype='text/csv')

@APP.route('/result.csv', methods=['POST'])
def result():
    """Calc and return result."""
    if 'studentfile' not in request.files:
        abort(400)

    with tempfile.TemporaryFile('w+') as temp_file:
        temp_file.write(str(request.files['studentfile'].read(),
                            encoding='utf-8'))
        temp_file.seek(0)
        manager = Manager(temp_file)

    rules.apply_all(manager)
    return Response(manager.get_result().to_csv(), mimetype='text/csv')

def run(app=APP):
    """Run app."""
    app.run(port=setting.PORT)
