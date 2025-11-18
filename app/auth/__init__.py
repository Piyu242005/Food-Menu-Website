"""
Authentication blueprint - Login, register, profile
"""
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes
