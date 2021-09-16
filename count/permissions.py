from rest_framework import permissions

class IsOwnerOrNotDelete(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        #삭제만 아니면 허용
        if request.method =='DELETE':
            return obj.user==request.user
        else:
            return True