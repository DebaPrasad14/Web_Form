# Generated by Django 2.1.4 on 2019-05-16 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0002_auto_20190516_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfield',
            old_name='job',
            new_name='job_title',
        ),
    ]
