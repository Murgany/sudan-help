# Generated by Django 4.2 on 2023-04-25 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudan_help', '0008_alter_medicalservice_closes_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_type',
            field=models.CharField(choices=[('Help needed', 'Help needed'), ('Available', 'Available')], max_length=100, verbose_name='Request type'),
        ),
    ]
