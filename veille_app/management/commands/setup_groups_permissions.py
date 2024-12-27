from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from veille_app.models import Category, Source, Content, Task, Report

class Command(BaseCommand):
    help = 'Setup default groups, users, and permissions'

    def handle(self, *args, **kwargs):
        # Créer les groupes et leurs permissions
        groups_permissions = {
            "Veilleur": [
                "add_content", "change_content", "delete_content",
                "add_source", "change_source", "delete_source",
                "view_task"
            ],
            "Analyste": [
                "view_content", "view_source", "view_task",
                "add_report", "change_report", "delete_report"
            ],
            "Décideur": [
                "view_content", "view_source", "view_report",
                "add_task", "change_task", "delete_task"
            ],
        }

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)

            # Assign permissions to the group
            for perm_codename in perms:
                try:
                    content_type = ContentType.objects.get_for_model(Content)
                    permission = Permission.objects.get(codename=perm_codename, content_type=content_type)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Permission {perm_codename} does not exist."))

            group.save()

        # Create users and assign them to the respective groups
        users_data = {
            "veilleur_user1": "Veilleur",
            "veilleur_user2": "Veilleur",
            "analyste_user1": "Analyste",
            "analyste_user2": "Analyste",
            "decideur_user1": "Décideur",
            "decideur_user2": "Décideur",
        }

        for username, group_name in users_data.items():
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password="password123")
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
                user.save()

        # Create a superuser
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(username="admin", password="adminpass", email="admin@example.com")

        self.stdout.write(self.style.SUCCESS('Default groups, users, and permissions created successfully.'))
