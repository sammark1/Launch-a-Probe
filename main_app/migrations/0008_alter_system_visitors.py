# Generated by Django 4.0.4 on 2022-04-21 17:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0007_system_visitors_alter_system_discoverer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='visitors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]