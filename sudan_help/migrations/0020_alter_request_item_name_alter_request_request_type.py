# Generated by Django 4.2 on 2023-04-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudan_help', '0019_alter_missingperson_last_seen_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='item_name',
            field=models.CharField(choices=[('food', 'Food'), ('drinking Water', 'Drinking Water'), ('medicine', 'Medicine'), ('transport', 'Transport'), ('accommodation', 'Accommodation')], max_length=100, verbose_name='Item name'),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_type',
            field=models.CharField(choices=[('help needed', 'Help needed'), ('available', 'Available')], max_length=100, verbose_name='Request type'),
        ),
    ]
