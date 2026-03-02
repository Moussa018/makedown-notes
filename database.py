from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings


#Defining how to connect to the database using environment variables
class Settings(BaseSettings):
    db_url: str
    
    class Config:
        env_file = ".env"
  
settings = Settings()      

#Creating the SQLAlchemy engine
engine = create_engine(settings.db_url)

#Creating a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Creating a base class for our models
Base = declarative_base()

