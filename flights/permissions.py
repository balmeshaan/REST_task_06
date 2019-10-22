from rest_framework.permissions import BasePermission
from datetime import date

class IsBookingOwnerOrStaff(BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.user == obj.user or request.user.is_staff:
			return True
		return False

class BookingIsThreeDaysAway(BasePermission):
	message = 'You can only modify this booking three days before its effective date'

	def has_object_permission(self, request, view, obj):
		if (obj.date - date.today()).days > 3:
			return True
		return False