# Generated by Django 2.2.6 on 2019-11-27 15:55

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemImage', models.ImageField(blank=True, null=True, upload_to='pic_folder/')),
                ('itemName', models.CharField(max_length=50)),
                ('itemDescription', models.CharField(max_length=500)),
                ('itemAdded', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('itemAuctonEnd', models.DateField()),
                ('itemPrice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('highestBidder', models.CharField(blank=True, max_length=50)),
                ('bidderList', models.CharField(blank=True, max_length=5000)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to='app.UserModel')),
            ],
        ),
    ]