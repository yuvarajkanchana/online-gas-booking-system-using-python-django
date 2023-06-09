# Generated by Django 2.2.6 on 2020-05-28 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gasbooking', '0005_bookcylinder_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_boy', models.CharField(max_length=100, null=True)),
                ('desc', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('time1', models.DateTimeField(null=True)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gasbooking.Bookcylinder')),
            ],
        ),
    ]
