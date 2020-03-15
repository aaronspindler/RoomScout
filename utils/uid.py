import uuid


def create_uid():
    id = uuid.uuid4()
    return str(id).split('-')[-1]
