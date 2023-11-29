from lib.user import User

class UserRepository:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["email_address"], row["username"])
            users.append(item)
        return users

    def find(self, user_id):
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [user_id])
        item = User(rows[0]["id"], rows[0]["email_address"], rows[0]["username"])
        return item

    def create(self, user):
        self._connection.execute('INSERT INTO users (email_address, username) VALUES (%s, %s)', 
            [user.email_address, user.username])
        return None

    def delete(self, user_id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [user_id])
        return None