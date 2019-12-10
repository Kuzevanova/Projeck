from flask import Blueprint


index = Blueprint('index', __name__, url_prefix='/')

@index.route('/')
@index.route('/index')
def get_index():
    return '''
    <html>
    <title>
        supermen rest
    </title>
    <body>
        <h3>Api:</h3>
        <a href="./api/persons">Persons</a>
        <a href="./api/schools">Schools</a>     
    </body>
    </html>'''
