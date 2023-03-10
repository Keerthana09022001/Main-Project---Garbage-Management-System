# Generated by Django 4.1.1 on 2022-11-19 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_remove_driver_allocatted_bin_delete_bins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bins',
            fields=[
                ('Bin_id', models.AutoField(primary_key=True, serialize=False)),
                ('Bin_name', models.CharField(max_length=100)),
                ('Bin_address1', models.CharField(max_length=100)),
                ('Bin_address2', models.CharField(max_length=100)),
                ('Bin_address3', models.CharField(max_length=100)),
                ('pincode', models.BigIntegerField()),
                ('distance_KM', models.CharField(max_length=100)),
                ('total_time', models.TimeField(default=0)),
                ('Bin_date', models.DateField(default=0)),
                ('Bin_status', models.CharField(max_length=50)),
                ('Bin_color', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Home.bin_color', verbose_name='bin_color')),
                ('Bin_location', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Home.location', verbose_name='region')),
                ('collections_day', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Home.scheduleingday', verbose_name='day')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='Allocatted_bin',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Home.bins', verbose_name='Bin_name'),
        ),
    ]
