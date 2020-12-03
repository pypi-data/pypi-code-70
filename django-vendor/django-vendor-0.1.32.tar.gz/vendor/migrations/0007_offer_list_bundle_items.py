# Generated by Django 3.1 on 2020-10-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_auto_20201005_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='list_bundle_items',
            field=models.BooleanField(default=False, help_text='When showing to customers, display the included items in a list?', verbose_name='List Bundled Items'),
        ),
    ]
