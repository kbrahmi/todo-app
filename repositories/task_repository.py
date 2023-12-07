from sqlalchemy.orm import Session


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db
