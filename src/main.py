from room import RoomManager
from flask import Flask, jsonify, request
from player import Player, Host
from room import Room, RoomManager
from cards import Cards


app = Flask(__name__)

room_manager = RoomManager()

@app.route("/")
def root():
    return "<p>Planning Poker</p>"

@app.route("/rooms", methods=["GET"])
def list_rooms():
    rooms = [room.to_dict() for room in room_manager.active_rooms()]
    return jsonify(rooms)

@app.route("/rooms", methods=["POST"])
def create_room():
    data = request.get_json()
    host_name = data.get("name")
    if not host_name:
        return jsonify({"error": "Name is required"}), 400
    host = Host(host_name)
    room = host.host_room(room_manager)
    return jsonify({"room": room.to_dict(), "host": host.to_dict()})


@app.route("/rooms/<room_id>", methods=["GET"])
def get_room(room_id):
    room = room_manager.get_room_by_id(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    return jsonify(room.to_dict())

@app.route("/rooms/<room_id>/join", methods=["POST"])
def join_room(room_id):
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    room = room_manager.get_room_by_id(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    player = Player(name)
    room.add_player(player)
    return jsonify({"room": room.to_dict(), "player": player.to_dict()})

@app.route("/rooms/<room_id>/play", methods=["POST"])
def play_card(room_id):
    pass

@app.route("/rooms/<room_id>/start", methods=["POST"])
def start_voting(room_id):
    pass

@app.route("/rooms/<room_id>/end", methods=["POST"])
def end_voting(room_id):
    pass

@app.route("/rooms/<room_id>/reset", methods=["POST"])
def reset_room(room_id):
    pass