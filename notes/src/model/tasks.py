# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок

import datetime
import

MY_NOTE = 'note.json'
ID = 0


def creation_note(head, body):
    global ID
    ID += 1
    time_date = datetime.datetime.now()
    date = f'{time_date:%d.%m.%Y}'
    time = f'{time_date:%H:%M:%S}'
    new_note = Note(ID, head, body, date, time)
    return new_note

    # with open(MY_NOTE, 'a') as note:
    #     note.writelines(info + ';')
    # note.close()


# note1 = creation_note('ytwefgc', 'adsvjiuh')
# note2 = creation_note('872r63', '8')
#
# print(note1.get_id())
# print(note2.get_id())
