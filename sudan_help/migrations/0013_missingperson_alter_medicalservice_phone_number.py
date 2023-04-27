# Generated by Django 4.2 on 2023-04-26 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudan_help', '0012_alter_medicalservice_closes_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissingPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('age', models.PositiveIntegerField(verbose_name='Age')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, verbose_name='Gender')),
                ('photo', models.ImageField(upload_to='missing_persons', verbose_name='Photo')),
                ('last_seen_location', models.CharField(blank=True, max_length=200, verbose_name='Last seen location')),
                ('last_seen_date', models.DateField(blank=True, verbose_name='Last seen sate')),
                ('description', models.TextField(blank=True, max_length=300, verbose_name='Description')),
                ('reported_by', models.CharField(max_length=200)),
                ('reported_at', models.DateTimeField(auto_now_add=True, verbose_name='Reported at')),
                ('reporters_phone_number', models.CharField(max_length=18, verbose_name="Reporter's phone number")),
            ],
            options={
                'verbose_name': 'Missing Person',
                'verbose_name_plural': 'Missing Persons',
            },
        ),
        migrations.AlterField(
            model_name='medicalservice',
            name='phone_number',
            field=models.CharField(max_length=18, verbose_name='Phone number'),
        ),
    ]