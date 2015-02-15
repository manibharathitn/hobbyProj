# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('payid', models.CharField(max_length=100)),
                ('hid', models.IntegerField()),
                ('city_code', models.IntegerField()),
                ('UNIQ', models.CharField(max_length=2)),
                ('Pending', models.IntegerField()),
                ('Booking', models.IntegerField()),
                ('Mobile', models.IntegerField()),
                ('RoomPrice', models.IntegerField()),
                ('booking_date', models.DateField(verbose_name='booking date')),
                ('checkin_date', models.DateField(verbose_name='checkin date')),
                ('checkout_date', models.DateField(verbose_name='checkout date')),
                ('cid_booking', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
