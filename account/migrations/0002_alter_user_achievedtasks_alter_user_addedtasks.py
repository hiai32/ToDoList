# Generated by Django 5.0.6 on 2024-06-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='achievedTasks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='addedTasks',
            field=models.IntegerField(default=0),
        ),
    ]
