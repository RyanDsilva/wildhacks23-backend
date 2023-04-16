from utils.database import Database

class Sequence(object):
    def __init__(self):
        self.db = Database()
        self.collection_name = 'sequence'

    def create(self, sequence):
        res = self.db.insert(sequence, self.collection_name)
        return res

    def find(self, sequence):
        return self.db.find(sequence, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, sequence):
        return self.db.update(id, sequence, self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)