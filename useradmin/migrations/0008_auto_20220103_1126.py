# Generated by Django 3.2.9 on 2022-01-03 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0007_auto_20220103_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ManyToManyField(to='useradmin.Group'),
        ),
    ]