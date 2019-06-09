# Generated by Django 2.2 on 2019-06-07 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0003_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='completed',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]