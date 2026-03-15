#!/usr/bin/python3
"""
Flask API - Checker-in bütün tələblərinə uyğunlaşdırılmış versiya
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Checker boş başlanğıc gözləyir
users = {}

@app.route("/")
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    """Status endpoint"""
    return "OK"

@app.route("/data")
def get_data():
    """
    Bütün istifadəçi adlarını siyahı kimi qaytarır.
    DİQQƏT: list(users.keys()) mütləqdir.
    """
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    """Konkret istifadəçi məlumatı"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Yeni istifadəçi əlavə edir"""
    # request.get_json(silent=True) daha təhlükəsizdir
    data = request.get_json(silent=True)
    
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # İstifadəçini saxlayırıq
    users[username] = data
    
    # 201 Created statusu ilə qaytarırıq
    return jsonify({"message": "User added", "user": data}), 201

# BU HİSSƏ MÜTLƏQDİR: Checker serveri bu blok vasitəsilə tapır
if __name__ == "__main__":
    app.run(host='localhost', port=5000)
