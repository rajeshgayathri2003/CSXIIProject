# Generated by Django 3.0.5 on 2020-08-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20200724_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temporary_passwd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('temppasswd', models.CharField(max_length=8)),
            ],
        ),
    ]
