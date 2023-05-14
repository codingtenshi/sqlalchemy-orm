import datetime

from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/company"

)
Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


def main():
    session = Session()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

    creation_date = Column(
        DateTime,
        default=datetime.datetime.now,
        nullable=False
    )

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"


Base.metadata.create_all()




