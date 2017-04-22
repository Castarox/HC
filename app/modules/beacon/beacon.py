import sqlite3
from sqlite3 import OperationalError

class Beacon:

    def __init__(self, beacon_adress, idx=0):
        self.connect = sqlite3.connect("cms.db")
        self.cur = self.connect.cursor()
        self.idx = idx
        self.beacon_adress = beacon_adress

    def save(self):
        """ Saves/updates beacon item in database """
        try:
            in_database = self.cur.execute("SELECT EXISTS(SELECT * FROM Beacon WHERE IDX=(?));", str(self.idx))
            in_database = in_database.fetchall()[0][0]
            if not in_database:
                self.cur.execute("INSERT INTO Beacon(BeaconIDX) VALUES(?);", [self.beacon_adress])
                self.connect.commit()
            elif in_database:
                self.cur.execute("UPDATE Beacon SET BeaconIDX=(?) WHERE IDX=(?);", [self.beacon_adress])
                self.connect.commit()

        except sqlite3.OperationalError as w:
            print("Cant add/edit this {}".format(w))

        except sqlite3.Error:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base')

    def delete(self):
        """ Removes beacon item from the database """
        try:
            self.cur.execute("DELETE FROM Beacon WHERE IDX=(?);", str(self.idx))
            self.connect.commit()

        except sqlite3.OperationalError as w:
            print("Cant delete this {}".format(w))

        except sqlite3.Error:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base')

    @classmethod
    def get_by_id(cls, id):
        """ Retrieves beacon item with given id from database.
        Args:
            id(int): item id
        Returns:
            Beacon: Beacon object with a given id
        """
        try:
            cls.connect = sqlite3.connect("cms.db")
            cls.cur = cls.connect.cursor()

            cls.cur.execute("SELECT * FROM Beacon WHERE IDX=(?);", [id])
            beacon = cls.cur.fetchall()[0]
            return Beacon(beacon[0], beacon[1])

        except sqlite3.OperationalError as w:
            print("Cant find this {}".format(w))

        except sqlite3.Error:
            if cls.connect:
                cls.connect.rollback()
                print('There was a problem with SQL Data Base')

    def close_database(self):
        self.connect.close()
