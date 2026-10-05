# from rest_framework.permissions import BasePermission

# class IsAuthenticated(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in ('GET','OPTIONS',"HEAD"):
#             return True
        

#         return self.request.user.is_authenticated