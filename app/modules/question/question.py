import sqlite3

class Question:

    def __init__(self, locationIDX, question, answer1, answer2, answer3, correctAnswer, idx=0):
        self.connect = sqlite3.connect("cms.db")
        self.cur = self.connect.cursor()
        self.idx=idx
        self.locationIDX = locationIDX
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.correctAnswer = correctAnswer


    def save(self):
        """ Saves location in database """
        try:
            in_database = self.cur.execute("SELECT EXISTS(SELECT * FROM Question WHERE IDX=(?));", str(self.idx))
            in_database = in_database.fetchall()[0][0]
            if not in_database:
                self.cur.execute("INSERT INTO Question(LocationIDX, Question, Answer1, Answer2, Answer3, CorrectAnswer) VALUES(?,?,?,?,?,?);",
                (self.locationIDX, self.question, self.answer1, self.answer2, self.answer3, self.correctAnswer))
                self.connect.commit()
            elif in_database:
                self.cur.execute("UPDATE Question SET LocationIDX=(?), Question=(?), Answer1=(?), Answer2=(?), Answer3=(?), CorrectAnswer=(?) WHERE IDX=(?);",
                                 (self.locationIDX, self.question, self.answer1, self.answer2, self.answer3, self.correctAnswer, str(self.idx)))
                self.connect.commit()

        except sqlite3.OperationalError as w:
            print("Cant add/edit this {}".format(w))

        except sqlite3.Error:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base')

    def delete(self):
        """ Removes question item from the database """
        try:
            self.cur.execute("DELETE FROM Question WHERE IDX=(?);", str(self.idx))
            self.connect.commit()

        except sqlite3.OperationalError as w:
            print("Cant delete this {}".format(w))

        except sqlite3.Error:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base')

    @classmethod
    def get_all(cls, locationIDX):
        """ Retrieves all Questions form database and returns them as list.
        Returns:
            list(question): list of all questions
        """
        try:
            # connect to database
            cls.connect = sqlite3.connect("cms.db")
            cls.cur = cls.connect.cursor()
            cls.question_list = []

            for item in cls.cur.execute("SELECT * FROM Question WHERE LocationIDX = (?);", [locationIDX]):
                cls.question_list.append(Question(item[0], item[1], item[2], item[3],item[4], item[5], item[6]))
            return cls.question_list

        except sqlite3.OperationalError as w:
            print("Cant get this {}".format(w))

        except sqlite3.Error:
            if cls.connect:
                cls.connect.rollback()

    @classmethod
    def get_by_id(cls, id):
        """ Retrieves question item with given id from database.
        Args:
            id(int): item id
        Returns:
            Question: Question object with a given id
        """
        try:
            cls.connect = sqlite3.connect("cms.db")
            cls.cur = cls.connect.cursor()

            cls.cur.execute("SELECT * FROM Question WHERE IDX=(?);", [id])
            question = cls.cur.fetchall()[0]
            return Question(question[0], question[1], question[2], question[3], question[4], question[5], question[6])

        except sqlite3.OperationalError as w:
            print("Cant find this {}".format(w))

        except sqlite3.Error:
            if cls.connect:
                cls.connect.rollback()
                print('There was a problem with SQL Data Base')

    def close_database(self):
        self.connect.close()