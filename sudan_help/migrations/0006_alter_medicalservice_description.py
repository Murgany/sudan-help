# Generated by Django 4.2 on 2023-04-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudan_help', '0005_alter_medicalservice_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalservice',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
    ]