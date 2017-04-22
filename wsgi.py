from app import app
from app.modules.sql.sql import Sql
from app.modules.question.question import Question
from app.modules.beacon.beacon import Beacon
from app.modules.location.location import Location



if __name__ == '__main__':
    Sql.load_database()
    # question1 = Question(1, "bla", "bla", "bleesdghsrth", "bla", "bla", )
    # question1.save()
    # bikon1 = Beacon(61)
    # bikon1.save()
    # lokacja1 = Location("fsf", 4)
    # lokacja1.save()
    app.run(debug=True)
