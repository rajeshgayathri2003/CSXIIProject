# Generated by Django 3.0.7 on 2020-06-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200623_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Add1',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.CharField(max_length=250),
        ),
    ]