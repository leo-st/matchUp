from sqlalchemy import Boolean, Column, Integer, String, text, ForeignKey, Identity
from sqlalchemy.orm import relationship
from models.permission_group import PermissionGroup

from db.sessions import Base

class Permission(Base):

    __tablename__ = 'Permission'
    __table_args__ = {'schema' : 'authsystem'}

    permission_id = Column(Integer, Identity(start=1, cycle=True), primary_key=True)
    permission_key = Column(String, nullable=False, server_default=text("'can_do_x'::text"))
    permission_group_id = Column(Integer, ForeignKey('authsystem.PermissionGroup.permission_group_id'), nullable=True)

    permission_group = relationship('PermissionGroup', back_populates='permissions', lazy='select')

    def to_response_dict(self):
        return {
            "permission_id": self.permission_id,
            "permission_key": self.permission_key,
            "permission_group_name": self.permission_group.permission_group_name
        }