from datetime import datetime
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime, Boolean, Unicode

engine = create_engine(os.environ.get("HEROKU_POSTGRESQL_WHITE_URL", "postgresql:///demo"))
session = scoped_session(sessionmaker(bind = engine, autoflush = False))

Base = declarative_base(bind = engine)

class SurveyResult(Base):
	__tablename__ = "survey_results"
	
	id = Column(Integer, primary_key = True, nullable = False)
	timestamp = Column(DateTime, nullable = False, index = True)
	ans1 = Column(Boolean, nullable = False)
	ans2 = Column(Integer, nullable = False)
	ans3 = Column(Unicode, nullable = False)
	
	def __init__(self, **kwargs):
		kwargs.setdefault("timestamp", datetime.utcnow())
		super(SurveyResult, self).__init__(**kwargs)