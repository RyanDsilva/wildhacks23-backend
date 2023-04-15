from utils.database import Database

class Dummy(object):
    def __init__(self):
        self.db = Database()
        self.collection_name = 'dummy'

    def create(self, dummy):
        res = self.db.insert(dummy, self.collection_name)
        return res

    def find(self, dummy):
        return self.db.find(dummy, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, dummy):
        return self.db.update(id, dummy, self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)