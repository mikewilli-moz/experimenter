# Generated by Django 3.2.23 on 2024-01-16 22:19

from django.db import migrations, models

from experimenter.experiments.constants import NimbusConstants


def set_default_qa_status(apps, schema_editor):
    NimbusExperiment = apps.get_model("experiments", "NimbusExperiment")
    NimbusExperiment.objects.filter(qa_status=None).update(
        qa_status=NimbusConstants.QAStatus.NOT_SET
    )


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0256_nimbusversionedschema_is_early_startup"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nimbusexperiment",
            name="qa_status",
            field=models.CharField(
                choices=[
                    ("RED", "Red"),
                    ("YELLOW", "Yellow"),
                    ("GREEN", "Green"),
                    ("NOT SET", "Not Set"),
                ],
                default="NOT SET",
                max_length=255,
                verbose_name="QA Status",
            ),
        ),
        migrations.RunPython(set_default_qa_status),
    ]
