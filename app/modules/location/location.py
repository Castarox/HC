import sqlite3

class Location:

    location_list = []

    def __init__(self, name, beacon_major, moderatorIDX, latitude, longitude, idx=0):
        self.connect = sqlite3.connect("cms.db")
        self.cur = self.connect.cursor()
        self.idx = idx
        self.name = name
        self.beacon_major = beacon_major
        self.moderatorIDX = moderatorIDX
        self.longitude = longitude
        self.latitude = latitude

    def save(self):
        """ Saves/updates location item in database """
        try:
            in_database = self.cur.execute("SELECT EXISTS(SELECT * FROM Location WHERE IDX=(?));", str(self.idx))
            in_database = in_database.fetchall()[0][0]
            if not in_database:
                self.cur.execute("INSERT INTO Location(Name, BeaconMajor, ModeratorIDX) VALUES(?,?,?);", (self.name, self.beacon_major, self.moderatorIDX))
                self.connect.commit()
            elif in_database:
                self.cur.execute("UPDATE Location SET Name=(?), BeaconMajor=(?), ModeratorIDX=(?), Latitude=(?), Longitude=(?) WHERE IDX=(?);", (self.name, self.beacon_major, self.moderatorIDX, self.latitude, self.longitude, self.idx))
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

    @classmethod
    def get_all(cls, moderatorIDX):
        """ Retrieves all Locations form database and returns them as list.
        Returns:
            list(location): list of all locations
        """
        try:
            # connect to database
            cls.connect = sqlite3.connect("cms.db")
            cls.cur = cls.connect.cursor()
            cls.location_list = []

            for item in cls.cur.execute("SELECT * FROM Location WHERE ModeratorIDX = (?);", [moderatorIDX]):
                cls.location_list.append(Location(item[0], item[1], item[2], item[3], item[4], item[5]))
            return cls.location_list

        except sqlite3.OperationalError as w:
            print("Cant get this {}".format(w))

        except sqlite3.Error:
            if cls.connect:
                cls.connect.rollback()

    @classmethod
    def get_by_id(cls, id):
        """ Retrieves location item with given id from database.
        Args:
            id(int): item id
        Returns:
            Location: Location object with a given id
        """
        try:
            cls.connect = sqlite3.connect("cms.db")
            cls.cur = cls.connect.cursor()

            cls.cur.execute("SELECT * FROM Location WHERE IDX=(?);", [id])
            location = cls.cur.fetchall()[0]
            return Location(location[1], location[2], location[3], location[4], location[5], location[0])

        except sqlite3.OperationalError as w:
            print("Cant find this {}".format(w))

        except sqlite3.Error:
            if cls.connect:
                cls.connect.rollback()
                print('There was a problem with SQL Data Base')