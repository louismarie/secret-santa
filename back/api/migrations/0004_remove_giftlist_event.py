# Generated by Django 3.2.12 on 2022-02-19 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_blacklist_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftlist',
            name='event',
        ),
    ]
