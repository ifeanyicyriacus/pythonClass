from src.diary_services.entry import Entry


class Diary:
    def __init__(self, username, password):
        self.entries:dict[int:Entry] = {}
        self.username = username
        self.password = password
        self.is_locked = True
        self.entry_id = 1


    @property
    def entries(self) -> dict[int, Entry]:
        return self.__entries
    @entries.setter
    def entries(self, entries: dict[int, Entry]):
        self.__entries = entries

    @property
    def is_locked(self):
        return self.__is_locked
    @is_locked.setter
    def is_locked(self, is_locked: bool):
        self.__is_locked = is_locked

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        if (username is not None) and (username != ''):
            self.__username = username
        else: raise ValueError('username cannot be empty')

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        if (password is not None) and (password != ''):
            self.__password = password
        else: raise ValueError('password cannot be empty')

    def unlock(self, password):
        if (password is None) or (password == ''):
            raise ValueError('password cannot be empty')
        if self.password == password:
            self.is_locked = False
        else:
            raise ValueError('password does not match')

    def lock(self):
        self.is_locked = True

    @property
    def number_of_entries(self):
        return len(self.entries)

    def create_entry(self, title, body):
        if self.is_locked:
            raise ValueError('cannot create entry for locked user')
        self.entries[self.entry_id] = Entry(self.entry_id, title, body)
        self.entry_id += 1

    def find_entry_by_id(self, entry_id) -> Entry:
        return self.entries[entry_id]


