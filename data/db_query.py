import sqlalchemy as sq
import os
from sqlalchemy.orm import sessionmaker
from models import *

base_name = 'тут название вашей базы данных'
DSN = f'sqlite:///{base_name}'
engine = sq.create_engine(DSN)
create_tables(engine)
print('hello')