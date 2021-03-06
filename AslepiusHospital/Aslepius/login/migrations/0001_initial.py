# Generated by Django 3.0.7 on 2020-06-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('patientid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('email', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=20)),
                ('confirmpasswd', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('Add1', models.CharField(max_length=30)),
                ('Add2', models.CharField(max_length=30)),
                ('Add3', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]
