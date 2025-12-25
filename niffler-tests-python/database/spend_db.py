from allure_commons.types import AttachmentType
from sqlalchemy import create_engine, Engine, event
from sqlmodel import Session, select

from models.spend import Spend


class SpendDb:
    engine: Engine

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        event.listen(self.engine, "do_execute", fn=self.attach_sql)

    @staticmethod
    def attach_sql(cursor, statement, parameters, context):
        statement_with_params = statement % parameters
        name = statement.split(" ")[0] + " " + context.engine.url.database
        allure.attach(statement_with_params, name=name, attachment_type=AttachmentType.TEXT)

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
