import os
from models.attachment import Attachment
from extensions import db
from werkzeug.utils import secure_filename
from config import Config

def save_attachment(expense_id, file):
    filename = secure_filename(file.filename)
    filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
    file.save(filepath)
    attachment = Attachment(expense_id=expense_id, filename=filename, filepath=filepath)
    db.session.add(attachment)
    db.session.commit()
    return attachment