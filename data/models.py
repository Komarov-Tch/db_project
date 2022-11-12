import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Genre(Base):
    """
    Тут пишите комментарий для класса,
    информацию, какие есть методы, и
    зачем он нужен вообще, желательно на английском
    """

    __tablename__ = 'genre'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)


class Autor(Base):
    """
    Тут комментарий про класс Autor
    """
    __tablename__ = 'autor'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    name = sq.Column(sq.String, nullable=False)
    surname = sq.Column(sq.String, nullable=False)
    nickname = sq.Column(sq.String, nullable=False)


class AutorBook(Base):
    """
    Тут комментарий про класс AutorBook
    """
    __tablename__ = 'autor_book'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    id_autor = relationship(Autor, backref='autor_book')
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)


class Book(Base):
    """
    Тут комментарий про класс Book
    """
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)
    date = sq.Column(sq.Integer, nullable=True)
    rating = sq.Column(sq.String, nullable=True)
    pages = sq.Column(sq.Integer, nullable=True)
    publishinghouse = sq.Column(sq.Integer, sq.ForeignKey('publishinghouse.id'), nullable=True)


class PublishingHouse(Base):
    """
    Тут комментарий про класс PublishingHouse
    """
    __tablename__ = 'publishinghouse'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)
    country = sq.Column(sq.Integer, sq.ForeignKey('country.id'), nullable=True)


class Country(Base):
    """
    Тут комментарий про класс Country
    """
    __tablename__ = 'country'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
