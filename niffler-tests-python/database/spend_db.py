

from sqlalchemy import create_engine, Engine
from sqlmodel import Session, select

from models.spend import Spend


class SpendDb:
    engine: Engine

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)

    def get_spend_in_db(self, username: str):
        with Session(self.engine) as session:
            spend = select(Spend).where(Spend.username == username)
            result = session.exec(spend).all()
            return result

    def delete_spend_in_db(self, spend_uid: str):
        with Session(self.engine) as session:
            spend = session.get(Spend, spend_uid)
            session.delete(spend)
            session.commit()
