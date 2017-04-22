from app.modules.sql import sql
import sqlite3


class User:

    def __init__(self, login, password, level, status, idx=0):
        self.connect = sqlite3.connect("cms.db")
        self.cur = self.connect.cursor()
        self.idx = idx
        self.login = login
        self.password = password
        self.level = level
        self.status = status

    def save(self):
        """ Saves/updates user item in database """
        try:
            in_database = self.cur.execute("SELECT EXISTS(SELECT * FROM User WHERE IDX=(?));", str(self.idx))
            in_database = in_database.fetchall()[0][0]
            if not in_database:
                self.cur.execute("INSERT INTO User(Login, Password, Level, Status) VALUES(?,?,?,?);",
                (self.login, self.password, self.level, self.status))
                self.connect.commit()
            elif in_database:
                self.cur.execute("UPDATE User SET Login=(?), Password=(?), Level=(?), Status=(?) WHERE IDX=(?);",
                                 (self.login, self.password, self.level, self.status, str(self.idx)))
                self.connect.commit()

        except sqlite3.OperationalError as w:
            print("Cant add/edit this {}".format(w))

        except sqlite3.Error:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base')

    def delete(self):
        """ Removes user item from the database """
        try:
            self.cur.execute("DELETE FROM User WHERE IDX=(?);", str(self.idx))
            self.connect.commit()

        except sqlite3.OperationalError as w:
            print("Cant delete this {}".format(w))

        except sqlite3.Error:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base')

    @staticmethod
    def findUser(user_login, user_password):
        try:
            connect = sqlite3.connect('cms.db')
            cur = connect.cursor()
            cur.execute("SELECT * FROM `User` WHERE Login =(?) AND Password =(?)", (user_login, user_password))
            connect.commit()
            user = cur.fetchall()[0]
            if (user):
                return User(user[1], user[2], user[3], user[4], user[0])
            else:
                return None
            
        except sqlite3.Error:
            if connect:
                connect.rollback()
                print('There was a problem with SQL Data Base')
        finally:
            if connect:
                connect.close()

