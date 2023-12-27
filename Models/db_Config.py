from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

Base = declarative_base()

postgre_path = 'postgresql://'+os.getenv('postgre_host')+':'+os.getenv('postgre_pass')+'@localhost:5432/Library'
engine = create_engine(postgre_path)

Session = sessionmaker(bind=engine)
session = Session()
