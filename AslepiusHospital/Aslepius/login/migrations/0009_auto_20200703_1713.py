# Generated by Django 3.0.7 on 2020-07-03 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20200703_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='passwd',
        ),
    ]
