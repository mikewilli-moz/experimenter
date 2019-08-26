# Generated by Django 2.1.7 on 2019-04-18 22:50

from django.db import migrations, models
from experimenter.experiments.constants import ExperimentConstants


def populate_risk_external_team_impact(apps, schema_editor):
    Experiment = apps.get_model("experiments", "Experiment")
    filtered_experiments = Experiment.objects.filter(
        status__in=[
            ExperimentConstants.STATUS_SHIP,
            ExperimentConstants.STATUS_ACCEPTED,
            ExperimentConstants.STATUS_LIVE,
            ExperimentConstants.STATUS_COMPLETE,
            "Rejected",
        ]
    )
    filtered_experiments.filter(risk_external_team_impact=None).update(
        risk_external_team_impact=False
    )


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0047_remove_experiment_addon_testing_url")
    ]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="risk_external_team_impact",
            field=models.NullBooleanField(default=None),
        ),
        migrations.RunPython(populate_risk_external_team_impact),
    ]
