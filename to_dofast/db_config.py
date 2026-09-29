from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///todo.db")

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Todoapp(Base):

    __tablename__ = "todoapp"

    id = Column(Integer, primary_key=True)

    title = Column(
        String(100),
        nullable=False
    )

    description = Column(
        String(500),
        nullable=False
    )

    priority = Column(
        String(20),
        nullable=False
    )

    is_completed = Column(
        Boolean,
        default=False
    )

    due_date = Column(
        Date,
        nullable=False
    )