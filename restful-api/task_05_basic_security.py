#!/usr/bin/python3
"""
API Security: Basic Auth, JWT və Role-based Access Control
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)

app = Flask(__name__)

# JWT və Təhlükəsizlik konfiqurasiyası
app.config['JWT_SECRET_KEY'] = 'holberton-super-secret-key'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Təlimatdakı API Specifications-a uyğun istifadəçi bazası
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password123"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("adminpass"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    """Basic Auth üçün şifrəni yoxlayır"""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Yalnız Basic Auth ilə girişə icazə verilir"""
    return jsonify({"message": "Basic Auth Access Granted"})

@app.route("/login", methods=["POST"])
def login():
    """Giriş edərək JWT tokeni yaradır"""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
        
    username = data.get("username")
    password = data.get("password")
    
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Role məlumatını tokenin içinə əlavə edirik
        access_token = create_access_token(
            identity=username, 
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Bad username or password"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Yalnız etibarlı JWT tokeni ilə giriş"""
    return jsonify({"message": "JWT Access Granted"})

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Yalnız admin rolu olanlar üçün"""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access Granted"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
