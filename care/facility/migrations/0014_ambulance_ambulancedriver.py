# Generated by Django 2.2.11 on 2020-03-22 16:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0013_auto_20200322_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('owner_name', models.CharField(max_length=255)),
                ('owner_phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(code='invalid_mobile', message='Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>', regex='^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$')])),
                ('owner_is_smart_phone', models.BooleanField(default=True)),
                ('primary_district', models.IntegerField(choices=[(1, 'Thiruvananthapuram'), (2, 'Kollam'), (3, 'Pathanamthitta'), (4, 'Alappuzha'), (5, 'Kottayam'), (6, 'Idukki'), (7, 'Ernakulam'), (8, 'Thrissur'), (9, 'Palakkad'), (10, 'Malappuram'), (11, 'Kozhikode'), (12, 'Wayanad'), (13, 'Kannur'), (14, 'Kasaragod')])),
                ('secondary_district', models.IntegerField(choices=[(1, 'Thiruvananthapuram'), (2, 'Kollam'), (3, 'Pathanamthitta'), (4, 'Alappuzha'), (5, 'Kottayam'), (6, 'Idukki'), (7, 'Ernakulam'), (8, 'Thrissur'), (9, 'Palakkad'), (10, 'Malappuram'), (11, 'Kozhikode'), (12, 'Wayanad'), (13, 'Kannur'), (14, 'Kasaragod')])),
                ('third_district', models.IntegerField(choices=[(1, 'Thiruvananthapuram'), (2, 'Kollam'), (3, 'Pathanamthitta'), (4, 'Alappuzha'), (5, 'Kottayam'), (6, 'Idukki'), (7, 'Ernakulam'), (8, 'Thrissur'), (9, 'Palakkad'), (10, 'Malappuram'), (11, 'Kozhikode'), (12, 'Wayanad'), (13, 'Kannur'), (14, 'Kasaragod')])),
                ('has_oxygen', models.BooleanField()),
                ('has_ventilator', models.BooleanField()),
                ('has_suction_machine', models.BooleanField()),
                ('has_defibrillator', models.BooleanField()),
                ('insurance_valid_till_year', models.IntegerField(choices=[(2020, 2020), (2021, 2021), (2022, 2022)])),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.Facility')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AmbulanceDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(code='invalid_mobile', message='Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>', regex='^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$')])),
                ('is_smart_phone', models.BooleanField()),
                ('ambulance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.Ambulance')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
