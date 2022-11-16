import sqlalchemy as sq
import os
from sqlalchemy.orm import sessionmaker
from models import *


def add_genre(session, list_genre):
    for genre in list_genre:
        add_ = Genre(title=genre)
        session.add(add_)
    session.commit()



base_name = 'тут название вашей базы данных'
DSN = f'sqlite:///{base_name}'
engine = sq.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

list_genre = ('ужасы', 'триллер', 'комедия',
              'драма', 'фантастика', 'фентези',
              'документальные', 'мемуары', 'детектив', 'боевик')
add_genre(session, list_genre)

session.close()
