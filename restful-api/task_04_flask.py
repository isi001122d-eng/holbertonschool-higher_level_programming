#!/usr/bin/python3
"""API Security with Basic Auth and JWT Role-based Access"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt, get_jwt_identity
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'holberton-secret-key' # Standart key yoxla
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Təlimata uyğun istifadəçi strukturu
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password123"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("adminpass"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON"}), 400
    
    username = data.get("username")
    password = data.get("password")
    
    if username in users and check_password_hash(users[username]['password'], password):
        # Rolu tokenin içinə 'role' olaraq qoymaq mütləqdir
        access_token = create_access_token(identity=username, additional_claims={"role": users[username]['role']})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Bad username or password"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return jsonify({"message": "Access Granted"})

@app.route("/admin-only")
@jwt_required()
def admin_only():
    claims = get_jwt()
    # Şəkildəki 'Implement checks to ensure user's role matches' tələbi
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access Granted"})

# Basic Auth üçün qorunan endpoint
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth Access Granted"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
