# Generated by Django 5.0.6 on 2024-06-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='userId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
