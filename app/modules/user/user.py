from app.modules.sql import sql
import sqlite3


class User:

    def __init__(self, login, password, level, points, idx=0):
        self.connect = sqlite3.connect("cms.db")
        self.cur = self.connect.cursor()
        self.idx = idx
        self.login = login
        self.password = password
        self.level = level
        self.points = points

    def save(self):
        """ Saves/updates user item in database """
        try:
            in_database = self.cur.execute("SELECT EXISTS(SELECT * FROM User WHERE IDX=(?));", str(self.idx))
            in_database = in_database.fetchall()[0][0]
            if not in_database:
                self.cur.execute("INSERT INTO User(Login, Password, Level, Points) VALUES(?,?,?,?);",
                (self.login, self.password, self.level, self.points))
                self.connect.commit()
            elif in_database:
                self.cur.execute("UPDATE User SET Login=(?), Password=(?), Level=(?), Points=(?) WHERE IDX=(?);",
                                 (self.login, self.password, self.level, self.points, str(self.idx)))
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

    def get_by_id(cls, id):
        """ Retrieves user item with given id from database.
        Args:
            id(int): item id
        Returns:
            User: User object with a given id
        """
        try:
            cls.connect = sqlite3.connect("cms.db")
            cls.cur = cls.connect.cursor()

            cls.cur.execute("SELECT * FROM User WHERE IDX=(?);", [id])
            user = cls.cur.fetchall()[0]
            return User(user[0], user[1], user[2], user[3], user[4])

        except sqlite3.OperationalError as w:
            print("Cant find this {}".format(w))

        except sqlite3.Error:
            if cls.connect:
                cls.connect.rollback()
                print('There was a problem with SQL Data Base')

    @staticmethod
    def findUser(user_login, user_password):
        connect = sqlite3.connect('cms.db')
        cur = connect.cursor()
        try:
            cur.execute("SELECT * FROM `User` WHERE Login =(?) AND Password =(?)", (user_login, user_password))
            try:
                user = cur.fetchall()[0]
            except:
                return None
            return User(user[1], user[2], user[3], user[4], user[0])

        except sqlite3.Error:
            if connect:
                connect.rollback()
                print('There was a problem with SQL Data Base')
        finally:
            if connect:
                connect.close()

