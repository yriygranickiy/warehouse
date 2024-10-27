from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.models import Base

db_url = "postgresql+psycopg2://my_user:qwerty@localhost:5438/my_db"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

