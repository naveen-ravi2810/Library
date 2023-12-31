from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()


postgres_path = (
    "postgresql://"
    + os.getenv("postgre_host")
    + ":"
    + os.getenv("postgre_pass")
    + "@localhost:5432/Library"
)
engine = create_engine(postgres_path)

Session = sessionmaker(bind=engine)
session = Session()


# session = scoped_session(sessionmaker(autoflush=False, autocommit=False, bind=engine))
