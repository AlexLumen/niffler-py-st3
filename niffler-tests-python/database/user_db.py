from allure_commons.types import AttachmentType
from sqlalchemy import create_engine, Engine, event
from sqlmodel import Session, select
import allure
from models.user import User


class UserDb:
    engine: Engine

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        event.listen(self.engine, "do_execute", fn=self.attach_sql)

    @staticmethod
    def attach_sql(cursor, statement, parameters, context):
        statement_with_params = statement % parameters
        name = statement.split(" ")[0] + " " + context.engine.url.database
        allure.attach(statement_with_params, name=name, attachment_type=AttachmentType.TEXT)

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
