from flask import Blueprint, request, jsonify, current_app
from services.attachment_service import save_attachment
from utils.decorators import token_required

attachment_bp = Blueprint("attachments", __name__)

@attachment_bp.route("/upload", methods=["POST"])
@token_required
def upload(current_user_id):
    file = request.files["file"]
    expense_id = request.form["expense_id"]
    attachment = save_attachment(expense_id, file)
    return jsonify({"msg" : "File uploaded", "filename" : attachment.filename})