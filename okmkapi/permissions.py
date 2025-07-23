from rest_framework.permissions import BasePermission, SAFE_METHODS
from .secure.decrypt_data import decrypt_message


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            admin_id = view.kwargs.get('admin_id')
            decrypted_id = decrypt_message(admin_id)
            if  decrypted_id in ('5647453083','1081454204'):
                return True

        except:
            return False


        return False
