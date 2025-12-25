import allure

from allure_commons.types import AttachmentType
from sqlalchemy import create_engine, Engine, event
from sqlmodel import Session, select

from models.category import Category


class CategoriesDb:
    engine: Engine

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        event.listen(self.engine, "do_execute", fn=self.attach_sql)

    @staticmethod
    def attach_sql(cursor, statement, parameters, context):
        statement_with_params = statement % parameters
        name = statement.split(" ")[0] + " " + context.engine.url.database
        allure.attach(statement_with_params, name=name, attachment_type=AttachmentType.TEXT)

    def get_category_by_name(self, username: str, category_name: str):
        with Session(self.engine) as session:
            category = select(Category).where(
                Category.username == username,
                Category.name == category_name
            )
            return session.exec(category).first()

    def get_category_by_id(self, category_id: str):
        with Session(self.engine) as session:
            category = select(Category).where(Category.id == category_id)
            return session.exec(category).first()

    def delete_category(self, category_id: str):
        with Session(self.engine) as session:
            category = session.get(Category, category_id)
            session.delete(category)
            session.commit()
