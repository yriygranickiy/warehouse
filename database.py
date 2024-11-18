from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.models import Base

db_url = "postgresql://my_user:qwerty@db_warehouse:5432/my_db"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

