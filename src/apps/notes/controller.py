from datetime import datetime

from bson import ObjectId

from common.storage import storage


def save_note(user_id:str, note:str):
    document = dict(
        note=note,
        user=ObjectId(user_id),
        create_date=datetime.now(),
    )
    note = storage.notes.save(document)
    return {'user_id': str(note)}
