from flask import Flask
from extensions import db
from routes.auth_routes import auth_bp
from routes.group_routes import group_bp
from routes.expense_routes import expense_bp
from routes.settlement_routes import settlement_bp
from routes.attachment_routes import attachment_bp
from config import Config
from flask_cors import CORS  # ✅ Import this
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    CORS(app, resources={r"/*": {"origins": "*"}})  # Or specify origins you allow


    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(group_bp, url_prefix="/groups")
    app.register_blueprint(expense_bp, url_prefix="/expenses")
    app.register_blueprint(settlement_bp, url_prefix="/settlements")
    app.register_blueprint(attachment_bp, url_prefix="/attachments")

    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)