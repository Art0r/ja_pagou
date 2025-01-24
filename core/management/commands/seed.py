from os.path import isfile
from django.core.management.base import BaseCommand, CommandError
from core.factory import UserFactory
from django.core.management import call_command
import os

from core.models import User


class Command(BaseCommand):
    help = "reset and seed the database"

    def handle(self, *args, **options):

        if os.path.isfile('db.sqlite3'):
            os.remove('db.sqlite3')
        
        call_command('migrate')

        UserFactory.create_batch(100)

        User.objects.create_superuser('admin', 'admin@example.com', 'admin')

