# Generated by Django 4.1.6 on 2023-12-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_remove_job_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
