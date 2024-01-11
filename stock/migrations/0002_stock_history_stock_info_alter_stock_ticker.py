# Generated by Django 4.2.9 on 2024-01-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='history',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='info',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]