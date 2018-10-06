from flask import render_template
from app import app
from operations import get_table


@app.route('/')
@app.route('/index')
def index():
    cursor = get_table('shoes')
    header = [x[0] for x in cursor.description]
    content = cursor.fetchall()
    return render_template('index.html', header=header, content=content)
