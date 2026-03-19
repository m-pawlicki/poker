import uuid

class Player:
    def __init__(self, name):
        self.id = uuid.uuid8()
        self.name = name
        self.is_host = False
        self.played_card = ''
        self.room_id = None

    def play_card(self, card):
        self.play_card = card
        return self.played_card
    
    def join_room(self):
        pass

class Host(Player):
    def __init__(self):
        super().__init__
        self.is_host = True

    def host_room(self):
        pass

    def change_story(self, room, story):
        pass 

    def call_vote(self):
        pass

    def end_vote(self):
        pass

    def invite_players(self):
        pass