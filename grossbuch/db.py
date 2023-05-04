from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

db_uri = getenv("DATABASE_URL")
if db_uri:
    db_uri = db_uri.replace("postgres", "postgresql")
    engine = create_engine(db_uri)
else:
    raise ValueError("Please, provide DATABSE_URL")

SessionFactory = sessionmaker(bind=engine)
session = scoped_session(SessionFactory)


class Setter:
    def set_values(self, data):
        for item in data:
            setattr(self, item, data[item])


Base = declarative_base(cls=Setter)
Base.query = session.query_property()

from . import app

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()
