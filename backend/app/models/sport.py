from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, text, Identity
from sqlalchemy.orm import relationship
from models.role import Role

from db.sessions import Base

class Sport(Base):

    __tablename__ = 'Sport'
    __table_args__ = {'schema' : 'core'}

    id = Column(Integer, Identity(), nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    number_of_players = Column(Integer, nullable=True)
    
    def to_response_dict(self) -> dict:
        return {
            'id': self.id,
            'name':self.name,
            'description': self.description,
            'number_of_players': self.number_of_players
        }
    