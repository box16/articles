# Generated by Django 3.1.4 on 2021-01-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20210110_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.URLField(default='', max_length=250),
        ),
    ]
