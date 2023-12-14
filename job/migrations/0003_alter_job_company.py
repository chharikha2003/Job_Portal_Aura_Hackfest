# Generated by Django 4.1.6 on 2023-12-13 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
        ('job', '0002_job_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.employer'),
        ),
    ]