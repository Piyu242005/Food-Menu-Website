"""
Admin blueprint - Admin dashboard and management
"""
from flask import Blueprint

bp = Blueprint('admin', __name__)

from app.admin import routes
