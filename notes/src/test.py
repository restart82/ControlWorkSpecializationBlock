from model.tasks import *
from model.note import *
from datetime import date
import json

MY_NOTE = 'note.json'
MY_NOTE2 = 'note2.json'

# add_note('ksdhawd')



# print(note1.id)
# print(note1.body)
# print(note1.creation_date)
# print(note1.creation_date.)
# date_string = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
# date_string = f'{note1.creation_date:%d.%m.%Y}'

def creat():
    note1 = Note('1', 'qwertgcd', 'sbdvibivbiq', date.today(), '12')
    return note1

note1 = creat()
def add(new_note):
    with open(MY_NOTE, 'a') as note:
        note.write(new_note.body)
    note.close()

add(note1)

# trunk_template = [
#     'switchport trunk encapsulation dot1q', 'switchport mode trunk',
#     'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
# ]

trunk_template = {
    'head': note1.head,
    'body': note1.body,
    # 'date': date_string,
    'time': note1.creation_time
}

print(type(trunk_template))


to_json = {'aaa 9': trunk_template}

print(type(to_json))

# with open(MY_NOTE2, 'a') as f:
#     json.dump(to_json, f, sort_keys=True, indent=2)
# f.close()

# with open(MY_NOTE2, 'r', encoding='utf8') as f:
#     data = json.load(f)
#     data.update(to_json)
#     with open(MY_NOTE2, 'w', encoding='utf8') as fout:
#         json.dump(data, fout, sort_keys=True, indent=2)
#     fout.close()

# print(data)
# print(type(data))
#
# data.update(to_json)
# print(data)
# print(type(data))
#
# with open(MY_NOTE2, 'w') as f:
#     json.dump(data, f, sort_keys=True, indent=2)
# f.close()

# with open(MY_NOTE2) as f:
#     print(f.read())
# f.close()





