# Generated by Django 3.0.7 on 2020-07-03 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0007_auto_20200703_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='register',
            name='patientid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
