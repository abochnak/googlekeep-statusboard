from flask import Flask, abort, render_template

from secrets import ACCESS_TOKEN

from keep import get_todos

app = Flask(__name__)

@app.route('/<path:token>')
def display_keep(token):
    if token != ACCESS_TOKEN:
        return abort(403, description='Forbidden')

    todo_list = get_todos()
    return render_template('index.html', todos=todo_list)