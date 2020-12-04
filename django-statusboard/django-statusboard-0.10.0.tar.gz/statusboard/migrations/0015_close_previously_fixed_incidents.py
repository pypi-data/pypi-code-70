# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 06:34
from __future__ import unicode_literals

from django.db import migrations


def close_previously_fixed_incidents_forward(apps, schema_editor):
    """Close incidents that were fixed before introducing the "closed"
    attribute."""
    Incident = apps.get_model("statusboard", "incident")
    db_alias = schema_editor.connection.alias
    for i in Incident.objects.using(db_alias).order_by("-created").all():
        if i.updates.exists():
            i.closed = i.updates.latest("created").status == 3
            i.save()


def close_previously_fixed_incidents_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('statusboard', '0014_incident_closed'),
    ]

    operations = [
        migrations.RunPython(close_previously_fixed_incidents_forward,
                             close_previously_fixed_incidents_backward)
    ]
