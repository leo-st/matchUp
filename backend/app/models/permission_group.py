from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, text, Identity
from sqlalchemy.orm import relationship

from db.sessions import Base

class PermissionGroup(Base):
    __tablename__ = 'PermissionGroup'
    __table_args__ = {'schema' : 'authsystem'}

    permission_group_id = Column(Integer, Identity(start=1, cycle=True), primary_key=True)
    permission_group_name = Column(String, nullable=False, server_default=text("'permission_group_x'::text"))

    permissions = relationship('Permission', back_populates='permission_group', lazy='select')

    def to_response_dict(self):
        return {
            "permission_group_name": self.permission_group_name,
            "permissions": [per.to_response_dict() for per in self.permissions]
        }