# Generated by Django 3.0.5 on 2020-08-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_temporary_passwd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temporary_passwd',
            name='id',
        ),
        migrations.AlterField(
            model_name='temporary_passwd',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
