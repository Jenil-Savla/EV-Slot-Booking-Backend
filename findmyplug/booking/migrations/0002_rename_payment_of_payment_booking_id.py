# Generated by Django 3.2.9 on 2021-12-01 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_of',
            new_name='booking_id',
        ),
    ]
