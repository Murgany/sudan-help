# Generated by Django 4.2 on 2023-04-26 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudan_help', '0013_missingperson_alter_medicalservice_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingperson',
            name='last_seen_date',
            field=models.DateField(blank=True, verbose_name='Last seen date'),
        ),
    ]
