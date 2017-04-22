import sqlite3

class Location:

    location_list = []

    def __init__(self, name, beaconIDX, idx=0):
        self.idx = idx
        self.name = name
        self.beaconIDX = beaconIDX

    def save(self):
        """ Saves/updates location item in database """
        try:
            in_database = self.cur.execute("SELECT EXISTS(SELECT * FROM Location WHERE IDX=(?));", str(self.idx))
            in_database = in_database.fetchall()[0][0]
            if not in_database:
                self.cur.execute("INSERT INTO Location(LocationIDX) VALUES(?);", (self.name, self.beaconIDX))
                self.connect.commit()
            elif in_database:
                self.cur.execute("UPDATE Location SET LocationIDX=(?) WHERE IDX=(?);", (self.name, self.beaconIDX))
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
            self.cur.execute("DELETE FROM Location WHERE IDX=(?);", str(self.idx))
            self.connect.commit()

        except sqlite3.OperationalError as w:
            print("Cant delete this {}".format(w))

        except sqlite3.Error:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base')

    def close_database(self):
        self.connect.close()

    def get_all(cls):
        """ Retrieves all Locations form database and returns them as list.
        Returns:
            list(Todo): list of all locations
        """
        try:
            # connect to database
            cls.connect = sqlite3.connect("cms.db")
            cls.cur = cls.connect.cursor()
            cls.location_list = []

            for item in cls.cur.execute("SELECT * FROM Location;"):
                cls.location_list.append(Location(item[0], item[1], item[2]))
            return cls.location_list

        except sqlite3.OperationalError as w:
            print("Cant get this {}".format(w))

        except sqlite3.Error:
            if cls.connect:
                cls.connect.rollback()