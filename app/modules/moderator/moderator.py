from app.modules.sql import sql
import sqlite3


class Moderator:

    def __init__(self, login, password, idx=0):
        self.connect = sqlite3.connect("cms.db")
        self.cur = self.connect.cursor()
        self.idx = idx
        self.login = login
        self.password = password

    def save(self):
        """ Saves/updates moderator item in database """
        try:
            in_database = self.cur.execute("SELECT EXISTS(SELECT * FROM Moderator WHERE IDX=(?));", str(self.idx))
            in_database = in_database.fetchall()[0][0]
            if not in_database:
                self.cur.execute("INSERT INTO Moderator(Login, Password) VALUES(?,?);",
                (self.login, self.password))
                self.connect.commit()
            elif in_database:
                self.cur.execute("UPDATE Moderator SET Login=(?), Password=(?) WHERE IDX=(?);",
                                 (self.login, self.password, str(self.idx)))
                self.connect.commit()

        except sqlite3.OperationalError as w:
            print("Cant add/edit this {}".format(w))

        except sqlite3.Error:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base')

    def delete(self):
        """ Removes moderator item from the database """
        try:
            self.cur.execute("DELETE FROM Moderator WHERE IDX=(?);", str(self.idx))
            self.connect.commit()

        except sqlite3.OperationalError as w:
            print("Cant delete this {}".format(w))

        except sqlite3.Error:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base')

    @classmethod
    def get_by_id(cls, id):
        """ Retrieves moderator item with given id from database.
        Args:
            id(int): item id
        Returns:
            Moderator: Moderator object with a given id
        """
        try:
            cls.connect = sqlite3.connect("cms.db")
            cls.cur = cls.connect.cursor()

            cls.cur.execute("SELECT * FROM Moderator WHERE IDX=(?);", [id])
            moderator = cls.cur.fetchall()[0]
            return Moderator(moderator[1], moderator[2], moderator[0])

        except sqlite3.OperationalError as w:
            print("Cant find this {}".format(w))

        except sqlite3.Error:
            if cls.connect:
                cls.connect.rollback()
                print('There was a problem with SQL Data Base')

    @staticmethod
    def findModerator(moderator_login, moderator_password):
        connect = sqlite3.connect('cms.db')
        cur = connect.cursor()
        try:
            cur.execute("SELECT * FROM `Moderator` WHERE Login =(?) AND Password =(?)", (moderator_login, moderator_password))
            try:
                moderator = cur.fetchall()[0]
            except:
                return None
            return Moderator(moderator[1], moderator[2], moderator[0])

        except sqlite3.Error:
            if connect:
                connect.rollback()
                print('There was a problem with SQL Data Base')
        finally:
            if connect:
                connect.close()

    def close_database(self):
        self.connect.close()

