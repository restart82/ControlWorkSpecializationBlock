# Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки.


class Note:
    'Класс-сущность для полей заметки'
    def __init__(self, id, head, body, creation_date, creation_time):
        self.id = id
        self.head = head
        self.body = body
        self.creation_date = creation_date
        self.creation_time = creation_time

    def get_id(self):
        return self.id

    def get_head(self):
        return self.head

    def get_body(self):
        return self.body

    def get_creation_date(self):
        return self.creation_date

    def get_creation_time(self):
        return self.creation_time
