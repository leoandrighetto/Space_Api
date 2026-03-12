from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from ..extensions import db
from ..models import User


auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/register")
def register():
    data = request.get_json() or {}
    username = (data.get("username") or "").strip()
    password = (data.get("password") or "").strip()

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400

    existing = User.query.filter_by(username=username).first()
    if existing:
        return jsonify({"error": "username already exists"}), 409

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "user created"}), 201


@auth_bp.post("/login")
def login():
    data = request.get_json() or {}
    username = (data.get("username") or "").strip()
    password = (data.get("password") or "").strip()

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "invalid credentials"}), 401

    token = create_access_token(identity={"id": user.id, "username": user.username})
    return jsonify({"access_token": token})
