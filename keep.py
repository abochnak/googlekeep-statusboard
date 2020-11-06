import gkeepapi
from secrets import USERNAME, GOOGLE_TOKEN, DEFAULT

def get_api(name):
    keep = gkeepapi.Keep()
    keep.resume(USERNAME, GOOGLE_TOKEN)
    
    gnote = list(keep.find(name))

    if len(gnote) != 1:
        return None, None
    todolist = gnote[0]

    return keep, todolist

def get_todos(name):
    keep, todolist = get_api(name)
    return todolist

def mark_as_done(index, todo_name, checked, name):
    keep, gnote = get_api(name)
    if index >= len(gnote.items):
        return False
    print(gnote.items[index].text, todo_name)
    if gnote.items[index].text == todo_name:
        print('Setting to', checked)
        gnote.items[index].checked = checked
        keep.sync()
        return True
    return False
