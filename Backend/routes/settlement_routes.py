from flask import Blueprint, request, jsonify
from services.settlement_service import settle_up
from utils.decorators import token_required

settlement_bp = Blueprint("settlements", __name__)

@settlement_bp.route("/", methods=["POST"])
@token_required
def settlement(current_user_id):
    data = request.json
    settlement = settle_up(
        group_id=data["group_id"],
        paid_by=current_user_id,
        received_by=data["received_by"],
        amount=data["amount"]
    )
    return jsonify({"msg" : "Settlement recorded", "settlement_id" : settlement.id})