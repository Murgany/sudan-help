# Generated by Django 4.2 on 2023-04-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudan_help', '0016_alter_missingperson_report_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingperson',
            name='report_type',
            field=models.CharField(choices=[('missing', 'Missing'), ('found', 'Found')], default='', max_length=30, verbose_name='Report type'),
        ),
    ]
