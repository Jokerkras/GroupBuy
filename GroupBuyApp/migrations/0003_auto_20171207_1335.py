# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 10:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GroupBuyApp', '0002_auto_20171204_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password_hash', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
                ('cash', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterModelOptions(
            name='lot',
            options={},
        ),
        migrations.AddField(
            model_name='lot',
            name='usersJoin',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lot',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterIndexTogether(
            name='lot',
            index_together=set([]),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='lot',
            name='slug',
        ),
        migrations.AddField(
            model_name='lot',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='GroupBuyApp.Account'),
        ),
    ]
