#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)

# JWT konfiqurasiyası
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Real layihədə bunu gizli saxla
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# İstifadəçi datası (hashed passwords ilə)
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

# --- 1. Basic Authentication ---
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Siz Basic Auth ilə daxil oldunuz!"})

# --- 2. JWT Authentication ---

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and check_password_hash(users[username]['password'], password):
        # Role-u tokenin içində saxlayırıq (Role-based access üçün)
        access_token = create_access_token(identity=username, additional_claims={"role": users[username]['role']})
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Yanlış istifadəçi adı və ya şifrə"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Xoş gəldin {current_user}, bu JWT ilə qorunan zonadır."})

# --- 3. Role-based Access Control (Admin Only) ---
@app.route('/admin-only')
@jwt_required()
def admin_only():
    # Token-dən role məlumatını çıxarırıq
    from flask_jwt_extended import get_jwt
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Bu səhifə yalnız adminlər üçündür"}), 403
    
    return jsonify({"message": "Xoş gəldin Admin!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
