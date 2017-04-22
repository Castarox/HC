import sqlite3

class Question:

    def __init__(self, LocationIDX, Question, Answer1, Answer2, Answer3, CorrectAnswer):
        self.LocationIDX = LocationIDX
        self.Question = Question
        self.Answer1 = Answer1
        self.Answer2 = Answer2
        self.Answer3 = Answer3
        self.CorrectAnswer = CorrectAnswer


    def save(self):
        """ Saves location in database """
        base = sqlite3.connect('cms.db')
        cursor = base.cursor()
        params = [self.LocationIDX, self.Question, self.Answer1, self.Answer2, self.Answer3, self.CorrectAnswer]
        cursor.execute("INSERT INTO Question (LocationIDX, Question, Answer1, Answer2, Answer3, CorrectAnswer) VALUES (?, ?, ?, ?, ?, ?);", params)
        base.commit()
        base.close()
