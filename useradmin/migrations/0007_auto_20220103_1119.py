# Generated by Django 3.2.9 on 2022-01-03 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0006_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='gname',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(to='useradmin.User'),
        ),
    ]
