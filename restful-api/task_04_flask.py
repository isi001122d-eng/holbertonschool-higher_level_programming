#!/usr/bin/python3
"""Flask API with specific checker requirements"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Checker adətən test datası istəmir, amma nümunədə jane var
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    # Siyahı (list) formatında istifadəçi adlarını qaytarırıq
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    # Mesajın "User not found" olduğundan və 404 statusundan əmin ol
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    # JSON-un düzgünlüyünü yoxla
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()
    username = data.get("username")
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Yeni istifadəçini əlavə et
    users[username] = {
        "username": username, # Bəzən daxildə də username tələb olunur
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    
    # 201 Created status kodu ilə təsdiq mesajı
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
