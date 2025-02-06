from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, text, Identity, DateTime, UUID
from sqlalchemy.orm import relationship
from models.user import User
from models.feed  import Feed
import uuid
from db.sessions import Base
from datetime import datetime

class ChatGroup(Base):

    __tablename__ = 'ChatGroup'
    __table_args__ = {'schema' : 'messages'}

    id = Column(Integer, Identity(), unique=True, nullable=False)
    create_timestamp = Column(DateTime, nullable=False, default=datetime.now())
    last_sent_message = Column(DateTime, nullable=True)
    admin_user_id = Column(Integer, ForeignKey('authsystem.User.id'), nullable=False)
    feed_id = Column(UUID(as_uuid=True),ForeignKey('core.Feed.id'), nullable=False) 

    admin_user = relationship('User', backref='User', lazy='select', uselist=False)
    feed = relationship('Feed', backref='Feed', lazy='select', uselist=False)

    def to_response_dict(self) -> dict:
        return {
            'id': self.id,
            'create_timestamp':self.create_timestamp,
            'last_sent_message': self.last_sent_message,
            'admin_user_id': self.admin_user_id
        }
        
class Message(Base):

    __tablename__ = 'Message'
    __table_args__ = {'schema' : 'messages'}

    id = Column(Integer, Identity(), unique=True, nullable=False)
    create_timestamp = Column(DateTime, nullable=False)
    edit_timestamp = Column(DateTime, nullable=True)
    content = Column(String, nullable=False, default='')
    edit_content = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('authsystem.User.id'), nullable=False)
    chat_group_id = Column(Integer, ForeignKey('messages.ChatGroup.id'), nullable=False)

    user = relationship('User', backref='User', lazy='select', uselist=False)
    chat_group = relationship('ChatGroup', backref='ChatGroup', lazy='select', uselist=False)

    def to_response_dict(self) -> dict:
        return {
            'id': self.id,
            'create_timestamp':self.create_timestamp,
            'edit_timestamp': self.edit_timestamp,
            'content': self.content,
            'edit_content':self.edit_content,
            'user_id': self.user_id,
            'chat_group_id': self.chat_group_id
        }
        
class ChatGroupUsers(Base):

    __tablename__ = 'ChatGroupUsers'
    __table_args__ = {'schema' : 'messages'}

    id = Column(Integer, Identity(), unique=True, nullable=False)
    chat_group_id = Column(Integer, ForeignKey('messages.ChatGroup.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('authsystem.User.id'), nullable=False)
    add_timestamp = Column(DateTime, nullable=False)
    remove_timestamp = Column(DateTime, nullable=True)

    user = relationship('User', backref='User', lazy='select', uselist=False)
    chat_group = relationship('ChatGroup', backref='ChatGroup', lazy='select', uselist=False)

    def to_response_dict(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'chat_group_id': self.chat_group_id,
            'add_timestamp': self.add_timestamp,
            'remove_timestamp':self.remove_timestamp
        }