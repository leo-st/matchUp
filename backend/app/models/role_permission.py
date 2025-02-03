from sqlalchemy import Column, Integer, String, Boolean, text, Table, ForeignKey
from db.sessions import Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

class RolesPermissions(Base):
    __tablename__ = 'RolesPermissions'
    __table_args__ = {'schema' : 'authsystem'}
    
    role_id = Column(ForeignKey('authsystem.Role.role_id'), primary_key=True)
    permission_id = Column(ForeignKey('authsystem.Permission.permission_id'), primary_key=True)