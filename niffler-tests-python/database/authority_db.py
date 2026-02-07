from allure_commons.types import AttachmentType
from sqlalchemy import create_engine, Engine, event
from sqlmodel import Session, select

from models.authority import Authority, User


class AuthorityDb:
    engine: Engine

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        event.listen(self.engine, "do_execute", fn=self.attach_sql)

    @staticmethod
    def attach_sql(cursor, statement, parameters, context):
        statement_with_params = statement % parameters
        name = statement.split(" ")[0] + " " + context.engine.url.database
        allure.attach(statement_with_params, name=name, attachment_type=AttachmentType.TEXT)

    def get_authority_by_user_id(self, user_id: str):
        with Session(self.engine) as session:
            authority = select(Authority).where(Authority.user_id == user_id)
            return session.exec(authority).all()

    def get_user_by_user_name(self, username: str):
        with Session(self.engine) as session:
            statement = select(User).where(User.username == username)
            try:
                user = session.exec(statement).one()
            except Exception:
                user = None
            return user

    def delete_authority(self, user_id: str):
        with Session(self.engine) as session:
            authority_obj = select(Authority).where(Authority.user_id == user_id)
            authorities = session.exec(authority_obj).all()
            for authority in authorities:
                session.delete(authority)
                session.commit()
