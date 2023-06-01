# Generated by Django 2.2.2 on 2020-05-25 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Addstaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffid', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Newconnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen', models.CharField(max_length=100, null=True)),
                ('nationality', models.CharField(max_length=100, null=True)),
                ('merriedstatus', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('related', models.CharField(max_length=100, null=True)),
                ('fname', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('connection', models.CharField(max_length=100, null=True)),
                ('registration', models.CharField(max_length=100, null=True)),
                ('date', models.CharField(max_length=100, null=True)),
                ('zipcode', models.CharField(max_length=100, null=True)),
                ('img', models.FileField(null=True, upload_to='')),
                ('cost', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gasbooking.Registration')),
            ],
        ),
        migrations.CreateModel(
            name='Bookcylinder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gassize', models.CharField(max_length=100, null=True)),
                ('booknumber', models.CharField(max_length=100, null=True)),
                ('bookdate', models.CharField(max_length=100, null=True)),
                ('bookstatus', models.CharField(max_length=100, null=True)),
                ('reffercost', models.CharField(max_length=100, null=True)),
                ('responsetime', models.CharField(max_length=100, null=True)),
                ('assignto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gasbooking.Addstaff')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gasbooking.Newconnection')),
            ],
        ),
    ]
