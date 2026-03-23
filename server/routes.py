from server import app
from flask import jsonify, request, render_template
from .player import Player, Host
from .room import Room, RoomManager, VoteState
from .cards import Cards

room_manager = RoomManager()

@app.route("/api/room", methods=["GET"])
def list_rooms():
    rooms = [room.to_dict() for room in room_manager.active_rooms()]
    return jsonify(rooms)

@app.route("/api/room", methods=["POST"])
def create_room():
    data = request.get_json()
    host_name = data.get("name")
    if not host_name:
        return jsonify({"error": "Name is required"}), 400
    host = Host(host_name)
    room = host.host_room(room_manager)
    return jsonify({"room": room.to_dict(), "player": host.to_dict()}), 200


@app.route("/api/room/<room_id>", methods=["GET"])
def get_room(room_id):
    room = room_manager.get_room_by_id(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    return jsonify(room.to_dict()), 200

@app.route("/api/room/<room_id>", methods=["POST"])
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
    return jsonify({"room": room.to_dict(), "player": player.to_dict()}), 200

@app.route("/api/room/<room_id>/play", methods=["POST"])
def play_card(room_id):
    data = request.get_json()
    player_id = data.get("player_id")
    card = data.get("card")
    room = room_manager.get_room_by_id(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    player = room.get_player(player_id)
    if player is None:
        return jsonify({"error": "Player not found"}), 404
    if room.vote_state != VoteState.START:
        return jsonify({"error": "Voting hasn't started yet"}), 403
    if player.play_card(card) is None:
        return jsonify({"error": "Invalid card"}), 400
    return jsonify(player.to_dict()), 200

@app.route("/api/room/<room_id>/story", methods=["POST"])
def update_story(room_id):
    data = request.get_json()
    player_id = data.get("player_id")
    story = data.get("story")
    room = room_manager.get_room_by_id(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    player = room.get_player(player_id)
    if player is None:
        return jsonify({"error": "Player not found"}), 404
    if room.host_id != player_id:
        return jsonify({"error": "Only the host can set a story"}), 403
    player.change_story(room, story)
    return jsonify(room.to_dict()), 200


@app.route("/api/room/<room_id>/start", methods=["POST"])
def start_voting(room_id):
    data = request.get_json()
    player_id = data.get("player_id")
    room = room_manager.get_room_by_id(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    player = room.get_player(player_id)
    if player is None:
        return jsonify({"error": "Player not found"}), 404
    if room.host_id != player_id:
        return jsonify({"error": "Only the host can start voting"}), 403
    player.start_vote(room)
    return jsonify(room.to_dict()), 200


@app.route("/api/room/<room_id>/end", methods=["POST"])
def end_voting(room_id):
    data = request.get_json()
    player_id = data.get("player_id")
    room = room_manager.get_room_by_id(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    player = room.get_player(player_id)
    if player is None:
        return jsonify({"error": "Player not found"}), 404
    if room.host_id != player_id:
        return jsonify({"error": "Only the host can end voting"}), 403
    player.end_vote(room)
    return jsonify(room.to_dict()), 200

@app.route("/api/room/<room_id>/reset", methods=["POST"])
def reset_room(room_id):
    data = request.get_json()
    player_id = data.get("player_id")
    room = room_manager.get_room_by_id(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    player = room.get_player(player_id)
    if player is None:
        return jsonify({"error": "Player not found"}), 404
    if room.host_id != player_id:
        return jsonify({"error": "Only the host can reset the room"}), 403
    player.reset_room(room)
    return jsonify(room.to_dict()), 200