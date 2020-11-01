from flask import Flask, abort, render_template, request

from secrets import ACCESS_TOKEN

from keep import get_todos, mark_as_done

app = Flask(__name__)

@app.route('/<path:token>')
def display_keep(token):
    if token != ACCESS_TOKEN:
        return abort(403, description='Forbidden')

    todo_list = get_todos()
    return render_template('index.html', todos=todo_list, token=token)

@app.route('/<path:token>/check', methods=['POST'])
def checked(token):
    if token != ACCESS_TOKEN:
        return abort(403, description='Forbidden')
    json = request.get_json()
    print(json)
    index = json['index']
    name = json['name']
    checked = json['checked']
    if mark_as_done(int(index), name, checked.lower() == 'true'):
        return 'OK'
    return abort(500, description='Did not update')

        
    