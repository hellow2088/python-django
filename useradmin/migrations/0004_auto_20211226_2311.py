# Generated by Django 3.2.9 on 2021-12-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0003_auto_20211226_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='123@126.com', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(default='12'),
        ),
        migrations.AddField(
            model_name='user',
            name='nikename',
            field=models.CharField(default='Jone', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='123', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='Jone', max_length=50),
        ),
    ]
