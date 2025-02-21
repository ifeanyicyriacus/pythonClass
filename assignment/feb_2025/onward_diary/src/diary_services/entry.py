from datetime import datetime

class Entry:
    def __init__(self, entry_id, title, body):
        self.entry_id = entry_id
        self.__DATE_CREATED = datetime.now()
        self.title = title
        self.body = body

    @property
    def entry_id(self):
        return self._entry_id
    @entry_id.setter
    def entry_id(self, entry_id:int):
        self._entry_id = entry_id

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def body(self):
        return self._body
    @body.setter
    def body(self, body: str):
        self._body = body

    @property
    def date_created(self):
        date = str(self.__DATE_CREATED.date())
        time = str(self.__DATE_CREATED.time())[:8]
        return f"[{date}] - [{time}]"

    def update_title(self, new_title):
        if new_title == "":
            raise ValueError("Body field cannot be empty")
        else: self.title = new_title

    def update_body(self, new_body):
        if new_body == "":
            raise ValueError("Body field cannot be empty")
        else: self.body = new_body

    def __str__(self):
        entry = f"\033[1m({self.entry_id})\t{self.title}\033[0m\n"
        entry += f"\033[3m{self.date_created}\033[0m\n"
        entry += self.body
        return entry


