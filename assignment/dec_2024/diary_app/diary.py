from entry import Entry

class Diary:
    _diary_count = 0
    
    def __init__(self, name:str):
        self.diary_count += 1
        self.name = name
        self.is_locked = True
        self.entries = []
    
    @property
    def diary_count(self) -> int:
        return self._diary_count
    
    @diary_count.setter
    def diary_count(self, diary_count:int) -> None:
        self._diary_count = diary_count
    
    @property
    def name(self) -> str:
        return self._name
        
    @name.setter
    def name(self, name:str) -> None:
        self._name = name
        
    @property
    def is_locked(self) -> bool:
        return self._is_locked
        
    @is_locked.setter
    def is_locked(self, is_locked:bool) -> None:
        self._is_locked = is_locked
       
    @property
    def entries(self) -> list:
        return self._entries
    
    @entries.setter
    def entries(self, entries:list) -> None:
        self._entries = entries
    
    def add_entry(self, entry_subject:str, entry_body:str) -> Entry:
        if self.is_locked:
            return None
        else:
            new_entry = Entry(entry_subject, entry_body)
            entries = self.entries
            entries.append(new_entry)
            self.entries = entries
            return new_entry
            
    def find_entry_by_id(self, ID:int) -> Entry:
        for entry in self.entries:
            if entry.ID == ID:
                return entry
        return None
            
    
            
        
    def __str__(self) -> str:
        size = len(self.entries)
        no_of_entries = f"{size:>2} entries" if (size > 1) else f"{size:>2} entry"
        
        diary = f"\033[Diary: {self.name} - {no_of_entries}\033[0m\n"
        diary += self.display_diary_entries()
        return diary
        
    def display_diary_entries(self):
        entries = ""
        for entry in self.entries:
            entries += f"\033[1m({entry.ID:>2})\t{entry.entry_subject}\033[0m\n"
            entries += f"\033[3m{entry.timestamp}\033[0m\n"
            entries += f"{entry.entry_body}\n"
            entries += "-----------------------------------------------------\n"
        return entries
        
        
        
        
        
