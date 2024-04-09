from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    # Define the list display fields as needed
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
    # Define fieldsets or fields attribute to customize admin interface
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    # Remove 'username' from the fieldsets or exclude it if it's specified
    exclude = ('username',)  # Use exclude if 'username' is specified in the model
    ordering = ('email',)

    # Optionally, customize other admin options as needed

# Register the CustomUserAdmin with the CustomUser model
admin.site.register(User, CustomUserAdmin)





























# class CustomUserAdmin(UserAdmin):
#     """Define admin model for custom User model with no username field."""
#     # fieldsets = (
#     #     (None, {'fields': ('email', 'password')}),
#     #     (_('Personal info'), {'fields': ('first_name', 'last_name')}),
#     #     (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#     #                                    'groups', 'user_permissions')}),
#     #     (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     # )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ( 'first_name', 'last_name', 'email', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('email', 'first_name', 'last_name', 'is_staff')
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)


# admin.site.register(get_user_model(), CustomUserAdmin)