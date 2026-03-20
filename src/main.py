from room import RoomManager
from flask import Flask
from player import Player, Host
from room import Room, RoomManager


app = Flask(__name__)

room_manager = RoomManager()

@app.route("/")
def root():
    return "<p>Planning Poker</p>"