from flask import Blueprint, request, jsonify
from models.expense import Expense, Split
from services.split_service import calculate_splits
from extensions import db
from utils.decorators import token_required

expense_bp = Blueprint("expense", __name__)

@expense_bp.route("/add", methods=["POST"])
@token_required
def add_expense(current_user):
    data = request.get_json()
    expense = Expense(
        group_id = data["group_id"],
        title = data["title"],
        amount = data["amount"],
        paid_by = current_user.id
    )
    db.session.add(expense)
    db.session.commit()

    split_list = calculate_splits(data["split_type"], data["spilt_data"], expense.amount)
    for s in split_list:
        split = Split(
            expense_id = expense.id,
            user_id = s["user_id"],
            amount = s["amount"]
        )
        db.session.add(split)
    db.session.commit()
    return jsonify({"msg" : "Expense added"})