from flask import Blueprint, request, jsonify
from services.split_service import add_expense
from utils.decorators import token_required

expense_bp = Blueprint("expenses", __name__)

@expense_bp.route("/add", methods=["POST"])
@token_required
def add_expense(current_user_id):
    data = request.json
    expense = add_expense(
        group_id = data["group_id"],
        title = data["title"],
        amount = data["amount"],
        paid_by = current_user_id,
        splits=data["splits"]
    )
    
    return jsonify({"msg" : "Expense added", "expense_id" : expense.id})