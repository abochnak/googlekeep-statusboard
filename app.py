from flask import Flask, abort, render_template, request

from secrets import ACCESS_TOKEN, DEFAULT

from keep import get_todos, mark_as_done

app = Flask(__name__)

@app.route('/<path:token>')
def display_keep(token):
    if token != ACCESS_TOKEN:
        return abort(403, description='Forbidden')

    name = request.args.get('name')
    if not name:
        name = DEFAULT
    todo_list = get_todos(name)
    return render_template('index.html', todos=todo_list, token=token, list=name)

@app.route('/<path:token>/check', methods=['POST'])
def checked(token):
    if token != ACCESS_TOKEN:
        return abort(403, description='Forbidden')
    json = request.get_json()
    print(json)
    index = json['index']
    name = json['name']
    checked = json['checked']
    todo_list = json["list"]
    if mark_as_done(int(index), name, checked.lower() == 'true', todo_list):
        return 'OK'
    return abort(500, description='Did not update')

        
    