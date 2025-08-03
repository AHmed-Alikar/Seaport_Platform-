# from flask import Blueprint, request, jsonify,current_app
# from werkzeug.security import check_password_hash
# from app.models.user import User
# from app.extensions import db
# from flask_jwt_extended import create_access_token
# import jwt, datetime
# # Define the Blueprint
# auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/login', methods=['POST'])

# def login():
#     data = request.json
#     # For demo: hardcode admin
#     if data.get('username') == 'admin' and data.get('password') == 'admin123':
#         token = jwt.encode({
#             "username": "admin",
#             "role": "admin",
#             "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8)
#         }, current_app.config['SECRET_KEY'], algorithm="HS256")
#         return jsonify({"token": token})
#     return jsonify({"error": "Invalid credentials"}), 401
# app/routes/auth.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    # Demo-only hardcoded admin check
    if data.get('username') == 'admin' and data.get('password') == 'admin123':
        expires = datetime.timedelta(hours=8)
        # Use the JWT extension, not PyJWT.encode
        token = create_access_token(
            identity={'username': 'admin', 'role': 'admin'},
            expires_delta=expires
        )
        return jsonify(token=token), 200

    return jsonify(error="Invalid credentials"), 401
