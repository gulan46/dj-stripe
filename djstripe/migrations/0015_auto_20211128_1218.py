# Generated by Django 3.2.9 on 2021-11-28 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0014_webhookeventtrigger_stripe_trigger_account'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'get_latest_by': 'created'},
        ),
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together=set(),
        ),
    ]
