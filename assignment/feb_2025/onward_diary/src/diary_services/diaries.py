from src.diary_services.diary import Diary


class Diaries:
    def __init__(self):
        self.diaries:dict[int:Diary] = {}
    
    def size(self):
        return len(self.diaries)

    def add(self, username, password) -> None:
        if username == "" : raise ValueError("Username cannot be empty")
        if password == "" : raise ValueError("Password cannot be empty")
        if username in self.diaries: raise ValueError("Username already exists")
        new_diary:Diary = Diary(username, password)
        self.diaries[username] = new_diary

    def find_by_username(self, username) -> Diary:
        if username == "": raise ValueError("Username cannot be empty")
        if username not in self.diaries:
            raise ValueError("Username not found")
        return self.diaries[username]

    def delete(self, username, password):
        if username == "": raise ValueError("Username cannot be empty")
        if password == "": raise ValueError("Password cannot be empty")
        try:
            if password != self.diaries[username].password:
                raise ValueError("Password does not match")
            self.diaries.pop(username)
        except KeyError:
            raise ValueError("Username not found")
        except ValueError:
            raise ValueError("Password does not match")
