# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 17:47
from __future__ import unicode_literals

from django.db import migrations, models


def update_statuses(apps, schema_editor):
    Experiment = apps.get_model("experiments", "Experiment")
    ExperimentChangeLog = apps.get_model("experiments", "ExperimentChangeLog")

    Experiment.objects.filter(status="Created").update(status="Draft")
    ExperimentChangeLog.objects.filter(old_status="Created").update(old_status="Draft")
    ExperimentChangeLog.objects.filter(new_status="Created").update(new_status="Draft")

    Experiment.objects.filter(status="Pending").update(status="Review")
    ExperimentChangeLog.objects.filter(old_status="Pending").update(old_status="Review")
    ExperimentChangeLog.objects.filter(new_status="Pending").update(new_status="Review")

    Experiment.objects.filter(status="Launched").update(status="Live")
    ExperimentChangeLog.objects.filter(old_status="Launched").update(old_status="Live")
    ExperimentChangeLog.objects.filter(new_status="Launched").update(new_status="Live")


class Migration(migrations.Migration):
    dependencies = [("experiments", "0007_auto_20180424_2039")]

    operations = [
        migrations.AlterField(
            model_name="experiment",
            name="status",
            field=models.CharField(
                choices=[
                    ("Draft", "Draft"),
                    ("Review", "Review"),
                    ("Accepted", "Accepted"),
                    ("Live", "Live"),
                    ("Complete", "Complete"),
                    ("Rejected", "Rejected"),
                ],
                default="Draft",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="experimentchangelog",
            name="new_status",
            field=models.CharField(
                choices=[
                    ("Draft", "Draft"),
                    ("Review", "Review"),
                    ("Accepted", "Accepted"),
                    ("Live", "Live"),
                    ("Complete", "Complete"),
                    ("Rejected", "Rejected"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="experimentchangelog",
            name="old_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Draft", "Draft"),
                    ("Review", "Review"),
                    ("Accepted", "Accepted"),
                    ("Live", "Live"),
                    ("Complete", "Complete"),
                    ("Rejected", "Rejected"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.RunPython(update_statuses),
    ]
