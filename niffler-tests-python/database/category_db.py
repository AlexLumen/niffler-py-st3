import allure

from allure_commons.types import AttachmentType
from sqlalchemy import create_engine, Engine, event
from sqlmodel import Session, select
from utils.allure_helpers import attach_sql
from models.category import Category


class CategoriesDb:
    engine: Engine

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        event.listen(self.engine, "do_execute", fn=attach_sql)

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
