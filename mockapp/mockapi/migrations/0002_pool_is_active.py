# Generated by Django 4.1.3 on 2022-11-10 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
