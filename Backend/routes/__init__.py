from flask import Blueprint
from .auth_routes import auth_bp
from .group_routes import group_bp
from .expense_routes import expense_bp
from .attachment_routes import attachment_bp
from .settlement_routes import settlement_bp

api_bp = Blueprint("api", __name__)

api_bp.register_blueprint(auth_bp, url_prefix="/auth")
api_bp.register_blueprint(group_bp, url_prefix="/gropus")
api_bp.register_blueprint(expense_bp, url_prefix="/expenses")
api_bp.register_blueprint(attachment_bp, url_prefix="/attachemnts")
api_bp.register_blueprint(settlement_bp, url_prefix="/settlements")