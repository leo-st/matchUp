from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, text, Identity
from sqlalchemy.orm import relationship
from models.role import Role

from db.sessions import Base

# if TYPE_CHECKING:
#     from .item import Item  # noqa: F401


class User(Base):

    __tablename__ = 'User'
    __table_args__ = {'schema' : 'authsystem'}

    id = Column(Integer, Identity(), unique=True, nullable=False)
    username = Column(String, nullable=False, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    enabled = Column(Boolean, default=True, nullable=False)
    pw_hash = Column(String, nullable=False)
    pw_reset_required = Column(Boolean, default=True, nullable=False)
    role_id = Column(Integer, ForeignKey('authsystem.Role.role_id'), nullable=True)

    role = relationship('Role', backref='Role', lazy='select', uselist=False)

    def to_response_dict(self) -> dict:
        return {
            'user_id': self.id,
            'username':self.username,
            'email': self.email,
            'first_name': self.first_name,
            'enabled': self.enabled,
            'last_name': self.last_name,
            'role_name': str(self.role.role_name),
            'role_id': self.role_id,
            'permission_keys': list(self.role.permission_keys)
        }
    
    def to_medium_response_dict(self) -> dict:
        return {
            'user_id': self.id,
            'username':self.username,
            'email': self.email,
            'first_name': self.first_name,
            'enabled': self.enabled,
            'last_name': self.last_name,
            'role_name': str(self.role.role_name)
        }
    
    def to_minimal_response_dict(self) -> dict:
        return {
            "user_id": self.id,
            "user_name": f"{self.first_name} {self.last_name}"
        }