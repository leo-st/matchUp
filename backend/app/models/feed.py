from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, text, Identity, Uuid, DateTime
from sqlalchemy.orm import relationship
from models.role import Role
from models.sport import Sport
from db.sessions import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Feed(Base):

    __tablename__ = 'Feed'
    __table_args__ = {'schema' : 'core'}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creation_timestamp = Column(DateTime, nullable=False)
    edit_timestamp = Column(DateTime, nullable=True)
    user_id = Column(Integer,ForeignKey('authsystem.User.id'), nullable=False)
    description = Column(String, nullable=False)
    sport_id = Column(String,ForeignKey('core.Sport.id'), nullable=False)
    likes = Column(Integer, nullable=False, default=0)
    impacts = Column(Integer, nullable=False, default=0)
    
    sport = relationship('Sport', backref='Sport', lazy='select', uselist=False)
    user = relationship('User', backref='User', lazy='select', uselist=False)
    
    def to_response_dict(self) -> dict:
        return {
            'id': self.id,
            'creation_timestamp':self.creation_timestamp,
            'edit_timestamp': self.edit_timestamp,
            'user_id': self.user_id,
            'description': self.description,
            'sport_id':self.sport_id,
            'likes': self.likes,
            'impacts': self.impacts
        }
    