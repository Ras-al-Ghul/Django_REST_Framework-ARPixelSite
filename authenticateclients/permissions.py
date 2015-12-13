from rest_framework import permissions

class IsOwnerOrNothing(permissions.BasePermission):
	#custom permission
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return obj.user.username == request.user.username

		return obj.user.username == request.user.username
