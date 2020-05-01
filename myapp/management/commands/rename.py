from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Rename a Django project' 

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The New Django Project')


    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        files_to_rename = ['myproject/settings/base.py', 'myproject/wsgi.py', 'manage.py']
        folder_to_rename = 'myproject'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filename = file.read()

            filename = filename.replace('myproject', new_project_name)

            with open(f, 'w') as file:
                file.write(filename)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS('Project has been rename to %s' % new_project_name))
