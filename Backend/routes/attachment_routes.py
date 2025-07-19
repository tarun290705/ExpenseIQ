from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
from models.attachment import Attachment
from extensions import db
from utils.decorators import token_required

attachemt_bp = Blueprint("attachment", __name__)

@attachemt_bp.routes("upload/<int:expense_id>", methods=["POST"])
@token_required
def upload_receipt(current_user, expense_id):
    if "file" not in request.files:
        return jsonify({"msg" : "No file part"}), 400
    file = request.files["file"]
    if file.filename == '':
        return jsonify({"msg", "No selected file"}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    attachment = Attachment(expense_id=expense_id, filename=filename, filepath=filepath)
    db.session.add(attachment)
    db.commit()
    return jsonify({"msg" : "File uploaded successfully"})