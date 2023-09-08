from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os
import json

from random import choice, randint
from datetime import datetime

db = SQLAlchemy()

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    location = Column(String)

# Create the database and tables
engine = create_engine('sqlite:///eventbrite_data.db')
Base.metadata.create_all(engine)
