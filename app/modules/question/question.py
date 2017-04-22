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

    def close_database(self):
        self.connect.close()