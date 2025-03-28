# Generated by Django 3.1.8 on 2021-05-07 20:51

from django.db import migrations


def set_risk_questions_to_false(apps, schema_editor):
    NimbusExperiment = apps.get_model("experiments", "NimbusExperiment")
    NimbusExperiment.objects.all().exclude(status="Draft", publish_status="Idle").update(
        risk_revenue=False, risk_brand=False, risk_partner_related=False
    )


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0168_auto_20210503_1340"),
    ]

    operations = [
        migrations.RunPython(set_risk_questions_to_false),
    ]
