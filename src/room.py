from nanoid import generate
from player import Player, Host
from enum import Enum

class VoteState(Enum):
    NO = 0
    START = 1
    END = 2

class RoomManager:
    def __init__(self):
        self.room_list = []

    def add_room(self, room: Room):
        if room not in self.room_list:
            self.room_list.append(room)

    def remove_room(self, room: Room):
        if room in self.room_list:
            self.room_list.remove(room)
    
    def get_room_by_host_id(self, id):
        for room in self.room_list:
            if room.id == id:
                return room
            else:
                raise Exception("Room not found")


class Room:
    def __init__(self):
        self.id = generate(size=8)
        self.creator_id = None
        self.vote_state = VoteState.NO
        self.curr_story = ""
        self.player_list = []

    def create_room(self, player: Player):
        room = Room()
        room.creator_id = player.id
        return room

    def delete_room(self):
        pass

    def start_voting(self):
        self.vote_state = VoteState.START
    
    def end_voting(self):
        self.vote_state = VoteState.END

    
    def update_story(self, story):
        self.curr_story = story

    def add_player(self, player: Player):
        self.player_list.append(player)