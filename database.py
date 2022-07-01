from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
from config import db_settings
from sqlalchemy.ext.declarative import declarative_base

# Create database connection
SQLALCHAMY_DATABASE_URL = 'postgresql+psycopg2://' + db_settings.DB_USER + ':' + db_settings.DB_PASSWORD + '@' \
                          + db_settings.DB_HOST + ':' + db_settings.DB_PORT + '/' + db_settings.DB_NAME

# Create the Postgresql table.
engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, )

Base = declarative_base()


