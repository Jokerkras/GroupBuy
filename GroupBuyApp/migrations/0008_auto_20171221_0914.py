# Generated by Django 2.0 on 2017-12-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupBuyApp', '0007_lot_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='usersJoin',
            field=models.IntegerField(default=1),
        ),
    ]