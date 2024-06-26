from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _


class UserCustomAdmin(UserAdmin):
	list_display_links = ['first_name', 'email']
	fieldsets = (
		(None, {"fields": ("username", "password")}),
		(_("Personal info"), {"fields": ("first_name", "last_name", "surname", "email", 'birth_date')}),
		(
			_("Permissions"),
			{
				"fields": (
					"is_active",
					"is_staff",
					"is_superuser",
					"groups",
					"user_permissions",
				),
			},
		),
		(_("Important dates"), {"fields": ("last_login", "date_joined")}),
	)
	

admin.site.register(User, UserCustomAdmin)
