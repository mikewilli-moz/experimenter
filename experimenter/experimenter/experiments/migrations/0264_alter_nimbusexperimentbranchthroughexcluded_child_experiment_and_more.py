# Generated by Django 5.0.2 on 2024-02-26 19:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0263_remove_nimbusversionedschema_sets_prefs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nimbusexperimentbranchthroughexcluded",
            name="child_experiment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s_child",
                to="experiments.nimbusexperiment",
            ),
        ),
        migrations.AlterField(
            model_name="nimbusexperimentbranchthroughexcluded",
            name="parent_experiment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s_parent",
                to="experiments.nimbusexperiment",
            ),
        ),
        migrations.AlterField(
            model_name="nimbusexperimentbranchthroughrequired",
            name="child_experiment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s_child",
                to="experiments.nimbusexperiment",
            ),
        ),
        migrations.AlterField(
            model_name="nimbusexperimentbranchthroughrequired",
            name="parent_experiment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s_parent",
                to="experiments.nimbusexperiment",
            ),
        ),
    ]
