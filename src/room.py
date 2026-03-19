from nanoid import generate
from enum import Enum

class IsVoting(Enum):
    NO = 0
    START = 1
    END = 2

class RoomManager:
    def __init__(self):
        self.room_list = []

    def add_room(self, room):
        if room not in self.room_list:
            self.room_list.append(room)

    def remove_room(self, room):
        if room in self.room_list:
            self.room_list.pop(room)


class Room:
    def __init__(self):
        self.id = generate()
        self.creator_id = None
        self.vote_state = IsVoting.NO
        self.curr_story = ""
        self.players = []

    def create_room(self):
        pass

    def delete_room(self):
        pass

    def start_voting(self):
        self.vote_state = IsVoting.START
    
    def end_voting(self):
        self.vote_state = IsVoting.END

    
    def update_story(self, story):
        self.curr_story = story