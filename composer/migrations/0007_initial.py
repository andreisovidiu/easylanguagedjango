# Generated by Django 5.0.6 on 2024-05-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('composer', '0006_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategy', models.TextField(max_length=1000)),
            ],
        ),
    ]