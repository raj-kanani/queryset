# Generated by Django 4.0.3 on 2022-03-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryapp', '0004_alter_student_roll'),
    ]

    operations = [
        migrations.CreateModel(
            name='student1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('mark', models.IntegerField()),
                ('pass_date', models.DateField(max_length=20)),
                ('adddatetime', models.DateField(max_length=20)),
            ],
        ),
    ]
