#!/usr/bin/python3
"""
API Security: Basic Auth, JWT ve Custom Error Handlers
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)

app = Flask(__name__)

# Konfiqurasiya
app.config['JWT_SECRET_KEY'] = 'holberton-super-secret-key'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# API Specifications-a uyğun istifadəçi datası
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    """Basic Auth doğrulaması"""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

# --- Custom JWT Error Handlers (MÜTLƏQDİR) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err, payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err, payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err, payload):
    return jsonify({"error": "Fresh token required"}), 401

# --- Endpoints ---

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """URL: /basic-protected"""
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    """JWT Token yaradılması"""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Missing JSON"}), 400
    
    username = data.get("username")
    password = data.get("password")
    
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Role məlumatını payload-a əlavə edirik
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)
    return jsonify({"error": "Bad username or password"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """URL: /jwt-protected"""
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """URL: /admin-only (Role-based check)"""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
