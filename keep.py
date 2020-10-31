import gkeepapi
import keyring
from secrets import USERNAME, PASSWORD

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
for todo in todolist.items:
    print(todo)