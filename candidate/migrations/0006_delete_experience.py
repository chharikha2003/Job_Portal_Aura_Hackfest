# Generated by Django 5.0 on 2023-12-14 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_alter_experience_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Experience',
        ),
    ]