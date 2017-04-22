from app.modules.sql import sql

class User:

    def __init__(self, idx, login, password, level):
        self.idx =idx
        self.login = login
        self.password = password
        self.level = level


    @staticmethod
    def isUser(login, password):
        query = "SELECT * FROM `User` WHERE Login = ? AND Password = ?"
        user = sql.query(query, [login, password])
        if user:
            return True
