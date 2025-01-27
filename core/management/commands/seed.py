from os.path import isfile
from django.core.management.base import BaseCommand, CommandError
from core.factory import PaymentFactory, UserFactory
from django.core.management import call_command
import os

from core.models import User, Payment


class Command(BaseCommand):
    help = "reset and seed the database"

    def handle(self, *args, **options):

        if os.path.isfile('db.sqlite3'):
            os.remove('db.sqlite3')
        
        call_command('migrate')

        UserFactory.create_batch(100)
        PaymentFactory.create_batch(20)

        User.objects.create_superuser('admin', 'admin@example.com', 'admin')

