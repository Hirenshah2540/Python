# Generated by Django 4.2.4 on 2023-08-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0004_register_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]