from room import RoomManager
from flask import Flask


app = Flask(__name__)

room_manager = RoomManager()

@app.route("/")
def root():
    return "<p>Hello, World!</p>"