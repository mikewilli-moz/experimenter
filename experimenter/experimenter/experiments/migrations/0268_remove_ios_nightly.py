# Generated by Django 5.0.3 on 2024-03-25 17:29

from django.db import migrations


def update_ios_channel(apps, schema_editor):
    NimbusExperiment = apps.get_model("experiments", "NimbusExperiment")
    # Update proposed_duration where it's less than proposed_enrollment
    NimbusExperiment.objects.filter(application="ios", channel="nightly").update(
        channel="developer"
    )


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0267_alter_nimbusexperiment_application_and_more"),
    ]

    operations = [
        migrations.RunPython(update_ios_channel),
    ]
