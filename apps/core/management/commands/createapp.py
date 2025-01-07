import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a new Django app with API structure"

    def add_arguments(self, parser):
        parser.add_argument("app_name", type=str, help="The name of the app to create")

    def handle(self, *args, **kwargs):
        app_name = kwargs["app_name"]
        app_dir = f"apps/{app_name}"

        if os.path.exists(app_dir):
            self.stdout.write(self.style.ERROR(f'App "{app_name}" already exists.'))
            return

        # Create directories
        os.makedirs(f"{app_dir}/migrations", exist_ok=True)
        os.makedirs(f"{app_dir}/api/v1", exist_ok=True)

        # Create files with content
        files_with_content = {
            "apps.py": self.generate_apps_py(app_name),
            "models.py": self.generate_models_py(app_name),
            "admin.py": self.generate_admin_py(app_name),
            "__init__.py": "",
            "migrations/__init__.py": "",
            "api/v1/views.py": self.generate_views_py(app_name),
            "api/v1/serializers.py": self.generate_serializers_py(app_name),
            "api/v1/urls.py": self.generate_urls_py(app_name),
        }

        for file_name, content in files_with_content.items():
            self.create_file(f"{app_dir}/{file_name}", content)

        # Add app to settings
        self.add_app_to_settings(app_name)

        self.stdout.write(
            self.style.SUCCESS(
                f'Created app "{app_name}" with API structure successfully!'
            )
        )

    def create_file(self, path, content=""):
        with open(path, "w") as f:
            f.write(content)

    def generate_apps_py(self, app_name):
        return f"""from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class {app_name.capitalize()}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.{app_name}'
    verbose_name = _("{' '.join(app_name.split('-')).title()}")
"""

    def generate_models_py(self, app_name):
        return "from django.db import models\n\n"

    def generate_admin_py(self, app_name):
        return "from django.contrib import admin\n\n"

    def generate_views_py(self, app_name):
        return """from rest_framework.views import APIView
from rest_framework.response import Response

class SampleAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'message': 'Hello from API v1!'})
"""

    def generate_serializers_py(self, app_name):
        return "from rest_framework import serializers\n\n"

    def generate_urls_py(self, app_name):
        return """from django.urls import path
from .views import SampleAPIView

urlpatterns = [
    path('sample/', SampleAPIView.as_view(), name='sample-api'),
]
"""

    def add_app_to_settings(self, app_name):
        app_path = f"apps.{app_name}"
        settings_file = "config/settings/base.py"

        with open(settings_file, "r") as file:
            settings_content = file.readlines()

        if not any(f"'{app_path}'" in line for line in settings_content):
            custom_apps_start = next(
                (
                    i
                    for i, line in enumerate(settings_content)
                    if line.strip().startswith("CUSTOM_APPS = [")
                ),
                None,
            )

            if custom_apps_start is not None:
                insert_position = custom_apps_start + 1
                while (
                    insert_position < len(settings_content)
                    and settings_content[insert_position].strip() != "]"
                ):
                    insert_position += 1
                settings_content.insert(insert_position, f"    '{app_path}',\n")

            with open(settings_file, "w") as file:
                file.writelines(settings_content)
