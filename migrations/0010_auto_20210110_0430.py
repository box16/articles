# Generated by Django 3.1.4 on 2021-01-10 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20210110_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
        migrations.AlterField(
            model_name='score',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
    ]
