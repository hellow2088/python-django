# Generated by Django 3.1.7 on 2021-04-03 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0002_auto_20210403_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='org',
            field=models.CharField(max_length=20),
        ),
    ]
