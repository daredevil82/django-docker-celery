# Generated by Django 2.0.9 on 2018-12-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipeds_id', models.IntegerField(help_text='IPEDS unique institution ID', unique=True)),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=20)),
                ('FIPS', models.IntegerField()),
            ],
        ),
    ]
