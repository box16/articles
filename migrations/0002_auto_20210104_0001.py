# Generated by Django 3.1.4 on 2021-01-04 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interests',
            old_name='interest_index',
            new_name='interest_level',
        ),
    ]