# Generated by Django 3.2.9 on 2022-01-03 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0008_auto_20220103_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='gname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='group',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
