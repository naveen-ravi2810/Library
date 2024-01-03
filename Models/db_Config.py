from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from core.settings import settings

engine = create_engine(settings.database_uri)
Session = sessionmaker(bind=engine)
session = Session()
