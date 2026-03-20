
from nanoid import generate
from cards import Cards
from room import Room, RoomManager

class Player:
    def __init__(self, name: str):
        self.id = generate()
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
        room.remove_player(self.id)
        self.room_id = None

    def change_name(self, name):
        self.name = name
        return self.name

class Host(Player):
    def __init__(self, name: str):
        super().__init__(name)
        self.is_host = True

    def host_room(self, room_manager: RoomManager) -> Room:
        room = Room()
        room.set_host(self.id)
        room.add_player(self)
        self.room_id = room.id
        room_manager.add_room(room)
        return room

    def change_story(self, room: Room, story):
        room.update_story(story)

    def call_vote(self, room: Room):
        if room.creator_id == self.id:
            room.start_voting()

    def end_vote(self, room: Room):
        if room.creator_id == self.id:
            room.end_voting()

    def invite_players(self):
        return "Invite sent"