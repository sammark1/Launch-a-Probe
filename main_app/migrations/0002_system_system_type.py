# Generated by Django 4.0.4 on 2022-04-19 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='system_type',
            field=models.CharField(choices=[('s', 'solitary star'), ('b', 'binary system'), ('t', 'trinary system'), ('cl', 'star cluster'), ('sn', 'stellar nebula')], default='s', max_length=20),
            preserve_default=False,
        ),
    ]
