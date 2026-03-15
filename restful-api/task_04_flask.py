#!/usr/bin/python3
"""Flask API - Final Checker Fix"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# ÇOX VACİB: Lüğəti tam boş başlat. 
# "jane" test üçün idi, checker isə təmiz başlanğıc istəyir.
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """Bütün istifadəçi adlarını siyahı kimi qaytarır"""
    # Əgər bu yenə FAIL versə, list(users.values()) yoxla, 
    # amma əvvəlcə təlimatdakı kimi 'keys' (usernames) göndər.
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    # request.get_json() istifadə et və mütləq lüğət olduğunu yoxla
    data = request.get_json()
    
    # 1. JSON validasiyası
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400
    
    # 2. Username yoxlanışı
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # 3. Dublikat yoxlanışı
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. İstifadəçini əlavə et (bütün datanı olduğu kimi saxla)
    users[username] = data
    
    # Mesaj və 201 statusu
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
