import os

FLASK_APP=os.environ['FLASK_APP']
FLASK_ENV=os.environ['FLASK_ENV']
SECRET_KEY=os.environ['SECRET_KEY']

# sqlite database for development ... 
SQLITE_DB_FILE=os.environ["SQLITE_DB_FILE"]

# Postgres information
PG_DB_USERNAME=os.environ['PG_DB_USERNAME']
PG_DB_PASSWORD=os.environ['PG_DB_PASSWORD']
PG_DB_HOST=os.environ['PG_DB_HOST']
PG_DATABASE_NAME=os.environ['PG_DATABASE_NAME']
