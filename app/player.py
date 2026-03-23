
from nanoid import generate
from .cards import Cards
from .room import Room, RoomManager

class Player:
    def __init__(self, name: str):
        self.player_id = generate(size=10)
        self.name = name
        self.is_host = False
        self.played_card = ""
        self.room_id: str | None = None

    def play_card(self, card: str):
        if card in Cards.DECK:
            self.played_card = card
            return self.played_card
        return None
        
    def clear_card(self):
        self.played_card = ""
    
    def join_room(self, room: Room):
        room.add_player(self)

    def leave_room(self, room: Room):
        room.remove_player(self.player_id)
        self.room_id = None

    # Will need to handle case for if a host changes name
    #def change_name(self, name):
    #    self.name = name
    #    return self.name
    
    def to_dict(self):
        return {
            "player_id": self.player_id,
            "name": self.name,
            "is_host": self.is_host,
            "played_card": self.played_card,
            "room_id": self.room_id,
        }


class Host(Player):
    def __init__(self, name: str):
        super().__init__(name)
        self.is_host = True

    def host_room(self, room_manager: RoomManager) -> Room:
        room = Room()
        room.set_host(self.player_id)
        room.add_player(self)
        self.room_id = room.room_id
        room_manager.add_room(room)
        return room

    def change_story(self, room: Room, story: str):
        if room.host_id == self.player_id:
            room.update_story(story)

    def start_vote(self, room: Room):
        if room.host_id == self.player_id:
            room.start_voting()

    def end_vote(self, room: Room):
        if room.host_id == self.player_id:
            room.end_voting()

    def reset_room(self, room: Room):
        if room.host_id == self.player_id:
            room.reset()

    def invite_players(self):
        return "Invite sent"