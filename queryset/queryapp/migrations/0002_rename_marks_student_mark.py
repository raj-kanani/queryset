# Generated by Django 4.0.3 on 2022-03-15 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queryapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='marks',
            new_name='mark',
        ),
    ]