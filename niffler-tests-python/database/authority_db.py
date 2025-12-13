from sqlalchemy import create_engine, Engine
from sqlmodel import Session, select

from models.authority import Authority


class AuthorityDb:
    engine: Engine

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)

    def get_authority_by_user_id(self, user_id: str):
        with Session(self.engine) as session:
            authority = select(Authority).where(Authority.user_id == user_id)
            return session.exec(authority).all()

    def delete_authority(self, user_id: str):
        with Session(self.engine) as session:
            authority_obj = select(Authority).where(Authority.user_id == user_id)
            authorities = session.exec(authority_obj).all()
            for authority in authorities:
                session.delete(authority)
                session.commit()
