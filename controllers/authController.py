from utils.database import Database

class AuthController(object):
    def __init__(self):
        self.db = Database()
        self.collection_name = 'users'

    def create(self, user):
        res = self.db.insert(user, self.collection_name)
        return res

    def find(self, user):
        return self.db.find(user, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, user):
        return self.db.update(id, user, self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)