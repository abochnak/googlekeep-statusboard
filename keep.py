import gkeepapi
import keyring
from secrets import USERNAME, PASSWORD

def get_api():
    keep = gkeepapi.Keep()
    # keep.login(USERNAME, PASSWORD)
    # # <snip>
    # token = keep.getMasterToken()
    # keyring.set_password('google-keep-token', USERNAME, token)

    token = keyring.get_password('google-keep-token', USERNAME)
    keep.resume(USERNAME, token)
    
    gnote = list(keep.find('Alicia To-Do List'))

    if len(gnote) != 1:
        print("Too many lists!")
        exit(1)
    todolist = gnote[0]

    return keep, todolist

def get_todos():
    keep, todolist = get_api()
    return todolist

def mark_as_done(index, todo_name, checked):
    keep, gnote = get_api()
    if index >= len(gnote.items):
        return False
    print(gnote.items[index].text, todo_name)
    if gnote.items[index].text == todo_name:
        print('Setting to', checked)
        gnote.items[index].checked = checked
        keep.sync()
        return True
    return False
