from database import Base
from sqlalchemy import Column, String


# defining the tabel (sqlalchemy maps classes into tabes)
class DocInfo(Base):
    __tablename__ = 'keyphrases'

    file_name = Column(String, primary_key=True)
    keyphrases = Column(String)
