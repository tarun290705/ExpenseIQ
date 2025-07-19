from flask import Blueprint, request, jsonify
from models.expense import Expense, Split
from models.group import GroupMember
from extensions import db
from utils.decorators import token_required

summary_bp = Blueprint("summary", __name__)

@summary_bp.route("/balance/<int:group_id>", methods=["GET"])
@token_required
def get_balanced(current_user, group_id):
    expenses = Expense.query.filter_by(group_id=group_id).all()
    balances = {}
    for expense in expenses:
        splits = Split.query.filter_by(expense_id=expense.id).all()
        for s in splits:
            if s.user_id != expense.paid_by:
                balances[(s.user_id, expense.paid_by)] = balances.get((s.user_id, expense.paid_by), 0) + s.amount
        return jsonify({"balances" : balances})