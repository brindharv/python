# Generated by Django 5.0 on 2024-01-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2024-01-04'),
            preserve_default=False,
        ),
    ]
