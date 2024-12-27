
# Register your models here.

from django.contrib import admin
from .models import  Category, Source, Content, Task, Report

# Register models here
admin.site.register(Category)
admin.site.register(Source)
admin.site.register(Content)
admin.site.register(Task)
admin.site.register(Report)

# permission 

from django.contrib.auth.models import User, Group

class RestrictedAdminSite(admin.AdminSite):
    def has_permission(self, request):
        # Limite l'accès aux superusers uniquement
        return request.user.is_superuser

restricted_admin_site = RestrictedAdminSite(name="restricted_admin")

# N'enregistrez pas User et Group ici pour restreindre leur accès
restricted_admin_site.register(Content)
restricted_admin_site.register(Source)
restricted_admin_site.register(Task)
restricted_admin_site.register(Report)

# from .permissions.setup_groups_permissions import setup_groups_permissions

# setup_groups_permissions()
