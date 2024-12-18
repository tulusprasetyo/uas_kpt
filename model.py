from database import Database  # Pastikan file database.py juga tersedia

class Data:
    def __init__(self):
        self.db = Database()

    def get_data(self, query, values=None):
        return self.db.fetch(query, values)

    def insert_data(self, query, values):
        self.db.execute(query, values)

    def close(self):
        self.db.close()
