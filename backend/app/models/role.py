from sqlalchemy import Column, Integer, String, Boolean, text, Table, ForeignKey, Identity
from db.sessions import Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from models.permission import Permission
from models.role_permission import RolesPermissions

class Role(Base):

    __tablename__ = 'Role'
    __table_args__ = {'schema' : 'authsystem'}

    role_id = Column(Integer, Identity(start=5, cycle=True), primary_key=True)
    role_name = Column(String, nullable=False, server_default=text("'Neuer Benutzertyp'::text"))
    locked = Column(Boolean, default=True, nullable=False)

    permissions = relationship('Permission', secondary='authsystem.RolesPermissions')

    permission_keys = association_proxy('permissions', 'permission_key')
    permission_groups = association_proxy('permissions', 'permission_group')

    def to_response_dict(self) -> dict:
        return {
            "role_id": self.role_id,
            "role_name": self.role_name,
            "locked": self.locked,
            "permission_groups": [
                {
                    "permission_group_name": pg.permission_group_name,
                    "permissions": [p.to_response_dict() for p in self.permissions if p.permission_group.permission_group_name == pg.permission_group_name]
                }
                for pg in set(self.permission_groups)
            ]
        }
