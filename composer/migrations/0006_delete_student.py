# Generated by Django 5.0.3 on 2024-04-22 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('composer', '0005_rename_students_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]