# Generated by Django 4.2 on 2023-04-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone number')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Accommodation',
                'verbose_name_plural': 'Accommodations',
            },
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone number')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Food Item',
                'verbose_name_plural': 'Food Items',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone number')),
                ('open_from', models.DateTimeField(auto_now_add=True, verbose_name='Open From')),
                ('closes_at', models.DateTimeField(auto_now_add=True, verbose_name='Closes At')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Hospital',
                'verbose_name_plural': 'Hospitals',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone number')),
            ],
            options={
                'verbose_name': 'Medicine',
                'verbose_name_plural': 'Medicines',
            },
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('open_from', models.DateTimeField(auto_now_add=True, verbose_name='Open From')),
                ('closes_at', models.DateTimeField(auto_now_add=True, verbose_name='Closes At')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone number')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Pharmacy',
                'verbose_name_plural': 'Pharmacies',
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('gathering_point', models.CharField(max_length=200, verbose_name='Gathering point')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='time')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone number')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Transport',
                'verbose_name_plural': 'Transports',
            },
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Water',
                'verbose_name_plural': 'Water',
            },
        ),
    ]
