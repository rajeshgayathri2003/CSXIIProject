# Generated by Django 3.0.5 on 2020-12-31 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccines', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccines',
            name='checked',
        ),
    ]
