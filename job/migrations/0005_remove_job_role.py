# Generated by Django 4.1.6 on 2023-12-13 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_category_job_city_job_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='role',
        ),
    ]