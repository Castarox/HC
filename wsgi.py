from app import app
from app.modules.sql.sql import Sql

if __name__ == '__main__':
    Sql.load_database()
    app.run()