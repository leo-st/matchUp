from pydantic import BaseModel

from core.enums import ExtendedEnum

class PermissionKey(ExtendedEnum):
    USERS_CAN_VIEW_USER_LIST = 'users_can_view_user_list'
    USERS_CAN_CREATE_USER = 'users_can_create_user'
    USERS_CAN_EDIT_OTHER_USERS = 'users_can_edit_other_users'
    ROLES_CAN_VIEW_ROLE_LIST = 'roles_can_view_role_list'
    ROLES_CAN_CREATE_EDIT_ROLE = 'roles_can_create_edit_role'
    PERMISSIONS_CAN_VIEW_PERMISSION_LIST = 'permissions_can_view_permission_list'
    PAGES_CAN_VIEW_ARTICLES_SUPPLIER = 'pages_can_view_articles_supplier'

    ADMIN = "admin"
    MEDICAL_PERSONEL = "med_pers"
    SUPPLY_LOGISTIC_PERSONEL = "sup_log_pers"
    PROCUREMENT_PERSONEL = "proc_pers"

# Shared properties
class PermissionBase(BaseModel):
    pass

class PermissionCreate(PermissionBase):
    pass

class PermissionUpdate(PermissionBase):
    pass