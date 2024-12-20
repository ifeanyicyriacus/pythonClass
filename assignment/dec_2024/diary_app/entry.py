from datetime import datetime

class Entry:
    _entry_count = 0
    
    def __init__(self, entry_subject:str, entry_body:str):
        Entry._entry_count += 1
        self._ID = Entry._entry_count
        self._timestamp = datetime.now()
        
        self.entry_subject = entry_subject
        self.entry_body = entry_body
        
    def entry_count(self) -> int:
        return self._entry_count
        
    @property
    def ID(self) -> int:
        return self._ID
    
    @property
    def entry_subject(self) -> str :
        return self._entry_subject
    
    @entry_subject.setter
    def entry_subject(self, entry_subject:str) -> None:
        self._entry_subject = entry_subject
    
    @property
    def entry_body(self) -> str:
        return self._entry_body
        
    @entry_body.setter
    def entry_body(self, entry_body:str) -> None:
        self._entry_body = entry_body
        
    @property
    def timestamp(self):
        return str(self._timestamp)
    
    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp
    
    def __str__(self):
        entry = f"\033[1m({self.ID:>2})\t{self.entry_subject}\033[0m\n"
        entry += f"\033[3m{self.timestamp}\033[0m\n"
        entry += self.entry_body
        return entry
    
    
