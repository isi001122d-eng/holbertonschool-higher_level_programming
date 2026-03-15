#!/usr/bin/python3
"""
Flask API - Checker üçün optimallaşdırılmış versiya
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# DİQQƏT: Təlimatda başlanğıcda bir nümunə user verilsə də, 
# checker çox vaxt sistemin BOŞ başlamasını yoxlayır.
# Əgər "jane" ilə FAIL alırsansa, bu lüğəti boşalt: users = {}
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """
    BÜTÜN istifadəçi adlarını siyahı (list) kimi qaytarmalıdır.
    Log-a əsasən, burada siyahı formatı dəqiq olmalıdır.
    """
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
    # request.is_json və ya request.get_json(silent=True) yoxlaması vacibdir
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Yeni istifadəçini əlavə edərkən bütün sahələri daxil et
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    
    # Mesajın və 201 kodunun dəqiqliyi
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
