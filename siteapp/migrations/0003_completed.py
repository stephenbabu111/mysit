# Generated by Django 2.2 on 2019-06-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0002_complaints_donedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='completed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('service', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('regdate', models.DateTimeField()),
                ('donedate', models.DateTimeField()),
            ],
        ),
    ]
