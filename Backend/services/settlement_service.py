from models.settlement import Settlement
from extensions import db

def settle_up(group_id, paid_by, received_by, amount):
    settlement = settlement(group_id=group_id, paid_by=paid_by, received_by=received_by, amount=amount)
    db.session.add(settlement)
    db.session.commit()
    return settlement