# Generated by Django 4.1.6 on 2025-01-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
