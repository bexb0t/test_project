from datetime import datetime
import os
import logging

from sqlalchemy import (
    Integer,
    String,
    create_engine as create_sqlalchemy_engine,
    Column,
    insert,
)
from sqlalchemy.orm import Session as SQLAlchemySession, DeclarativeBase
from sqlmodel import Field, SQLModel, Session, create_engine as create_sqlmodel_engine


class Base(DeclarativeBase):
    pass


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# get env vars
MYSQL_HOST = os.environ["MYSQL_HOST"]
MYSQL_DATABASE = os.environ["MYSQL_DATABASE"]
MYSQL_PORT = os.environ["MYSQL_PORT"]
MYSQL_ADMIN_USER = os.environ["MYSQL_ADMIN_USER"]
MYSQL_ADMIN_PASSWORD = os.environ["MYSQL_ADMIN_PASSWORD"]

DATABASE_URL = f"mysql://{MYSQL_ADMIN_USER}:{MYSQL_ADMIN_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

# SQLAlchemy connetion
sqlalchemy_engine = create_sqlalchemy_engine(DATABASE_URL, echo=True)

# SQLModel
sqlmodel_engine = create_sqlmodel_engine(DATABASE_URL, echo=True)


class SQLAlchemyTestModel(Base):  # type: ignore
    __tablename__ = "testmodel"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class SQLModelTestModel(SQLModel, table=True):  # type: ignore
    __tablename__ = "testmodel"
    id: int | None = Field(default=None, primary_key=True)
    name: str


def insert_data_sqlalchemy(session: SQLAlchemySession, num_rows: int):
    data = [{"name": f"sqlalchemy_{i}"} for i in range(num_rows)]
    session.execute(insert(SQLAlchemyTestModel), data)
    session.commit()


def insert_data_sqlmodel(session: Session, num_rows: int):
    data = [SQLModelTestModel(name=f"sqlmodel_{i}") for i in range(num_rows)]
    session.add_all(data)
    session.commit()


def main():
    with SQLAlchemySession(sqlalchemy_engine) as session:
        start_time = datetime.now()
        insert_data_sqlalchemy(session, 10)
        end_time = datetime.now()
        print(f"SQLAlchemy insert time: {end_time - start_time} seconds")

    with Session(sqlmodel_engine) as session:
        start_time = datetime.now()
        insert_data_sqlmodel(session, 10)
        end_time = datetime.now()
        print(f"SQLModel insert time: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
