import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",  # Ganti dengan host MySQL Anda
            user="root",       # Ganti dengan user MySQL Anda
            password="password",  # Ganti dengan password MySQL Anda
            database="karyawan"   # Ganti dengan nama database Anda
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def fetch(self, query, values=None):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def execute(self, query, values=None):
        self.cursor.execute(query, values)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

