from datetime import datetime

from bson import ObjectId

from common.storage import storage


def get_user_per_page(page:int, per_page:int, query:dict=None):
    """

    :param page:Number of page
    :param per_page: Number the user per page
    :param query: query if is necessary
    :return: users' information
    """
    users = storage.users.collection.find(query).limit(per_page).skip((page - 1) * per_page)
    return users.count(), {'users': list(users)}

def get_user(user_id:str):
    user = storage.users.collection.find_one({'_id': ObjectId(user_id)})
    notes = storage.notes.collection.find({'user': ObjectId(user['_id'])})
    user.update({'notes': list(notes)})
    return {'user': user}

def save_user(username:str, lastname:str, old:int, gender:str, email:str):
    old_user = storage.users.collection.find_one({'email': email})
    if old_user:
        return {'error': 'duplicate user'}
    document = dict(
        username=username,
        lastname=lastname,
        old=old,
        gender=gender,
        email=email,
        create_date=datetime.now()
    )
    user = storage.users.collection.save(document)
    return {'user_id': str(user)}

def delete_user(user_id):
    user = storage.users.collection.delete_one({'_id': ObjectId(user_id)})
    return {'deletes': user.deleted_count}
