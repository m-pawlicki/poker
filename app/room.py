from enum import Enum
from nanoid import generate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .player import Player

class VoteState(Enum):
    END = 0
    START = 1

class RoomManager:
    def __init__(self):
        self.room_list = []

    def active_rooms(self):
        return self.room_list

    def add_room(self, room: Room):
        if room not in self.room_list:
            self.room_list.append(room)

    def remove_room(self, room: Room):
        if room in self.room_list:
            self.room_list.remove(room)

    def get_room_by_id(self, room_id: str):
        for room in self.room_list:
            if room.room_id == room_id:
                return room
        return None
    
    def find_room_by_host_id(self, host_id: str):
        for room in self.room_list:
            if room.host_id == host_id:
                return room
        return None
    
    def find_room_by_player_id(self, player_id: str):
        for room in self.room_list:
            for player in room.player_list:
                if player_id == player.player_id:
                    return room
        return None

    def remove_player_from_room(self, room_id: str, player_id: str):
        room = self.get_room_by_id(room_id)
        if room:
            room.remove_player(player_id)
            return True
        return False


class Room:
    def __init__(self):
        self.room_id = generate(size=6)
        self.host_id = None
        self.vote_state = VoteState.END
        self.story = ""
        self.player_list = []

    def set_host(self, host_id: str):
        self.host_id = host_id

    def add_player(self, player: Player):
        for entry in self.player_list:
            if entry.player_id == player.player_id:
                return
        player.room_id = self.room_id
        self.player_list.append(player)

    def remove_player(self, player_id: str):
        player = self.get_player(player_id)
        if player is not None:
            self.player_list.remove(player)

    def get_player(self, player_id: str):
        for player in self.player_list:
            if player.player_id == player_id:
                return player
        return None

    def start_voting(self):
        self.vote_state = VoteState.START
    
    def end_voting(self):
        self.vote_state = VoteState.END
    
    def reset(self):
        for player in self.player_list:
            player.clear_card()
        self.vote_state = VoteState.END
        self.clear_story()
    
    def update_story(self, story: str):
        self.story = story
    
    def clear_story(self):
        self.story = ""
    
    def to_dict(self):
        return {
            "room_id": self.room_id,
            "host_id" : self.host_id,
            "vote_state": self.vote_state.name,
            "story": self.story,
            "player_list": [player.to_dict() for player in self.player_list],
        }