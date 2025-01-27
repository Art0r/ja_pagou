# Generated by Django 4.2 on 2025-01-27 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.FloatField()),
                ('payier', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pauir_payment', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receiver_payment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]