# Generated by Django 2.2.6 on 2019-10-28 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_repository_pulp_type'),
        ('file', '0004_filefilesystemexporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileRepository',
            fields=[
                ('repository_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='file_filerepository', serialize=False, to='core.Repository')),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.repository',),
        ),
    ]
