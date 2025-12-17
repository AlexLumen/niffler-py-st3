

from sqlalchemy import create_engine, Engine
from sqlmodel import Session, select

from models.user import User


class UserDb:
    engine: Engine

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)

    def get_user_by_username(self, username: str):
        with Session(self.engine) as session:
            user = select(User).where(User.username == username)
            return session.exec(user).first()

    def get_user(self):
        with Session(self.engine) as session:
            user = select(User)
            return session.exec(user).first()


    def delete_user_by_id(self, user_uid: str):
        with Session(self.engine) as session:
            spend = session.get(User, user_uid)
            session.delete(spend)
            session.commit()
