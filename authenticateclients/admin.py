from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from authenticateclients.models import UploaderClient
#from authenticateclients.forms import UploaderClientCreationForm, UploaderClientChangeForm

class UploaderClientInline(admin.StackedInline):
    model = UploaderClient
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (UploaderClientInline,)

# Register your models here.

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
"""
class UploaderClientAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('accountname', 'company_name', 'vuforiadb_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = UploaderClientChangeForm
    add_form = UploaderClientCreationForm
    list_display = ('email', 'company_name', 'is_staff')
    search_fields = ('email', 'company_name')
    ordering = ('email',)

admin.site.register(UploaderClient, UploaderClientAdmin)

"""