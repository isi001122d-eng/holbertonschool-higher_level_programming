#!/usr/bin/python3
"""
Flask framework-ü ilə sadə bir REST API
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçiləri yaddaşda (in-memory) saxlamaq üçün lüğət
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    """Ana səhifə endpoint-i"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Sistemdəki bütün istifadəçi adlarını qaytarır"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """API-nin vəziyyətini qaytarır"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Dinamik marşrut: konkret istifadəçi məlumatlarını qaytarır"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """POST sorğusu vasitəsilə yeni istifadəçi əlavə edir"""
    # 1. JSON datanın olub-olmadığını yoxla
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # 2. Username sahəsinin olub-olmadığını yoxla
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # 3. İstifadəçinin artıq mövcud olub-olmadığını yoxla
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # 4. İstifadəçini əlavə et
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
