# Generated by Django 2.2.4 on 2019-08-22 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0036_auto_20190806_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message_user_2_user',
            name='id_old',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='id_old',
        ),
        migrations.RemoveField(
            model_name='messages_state',
            name='id_old',
        ),
        migrations.RemoveField(
            model_name='messages_theme',
            name='id_old',
        ),
        migrations.RemoveField(
            model_name='messages_theme_access',
            name='id_old',
        ),
    ]
