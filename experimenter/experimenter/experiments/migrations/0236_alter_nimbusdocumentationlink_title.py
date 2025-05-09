# Generated by Django 3.2.19 on 2023-05-30 13:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0235_auto_20230512_1934"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nimbusdocumentationlink",
            name="title",
            field=models.CharField(
                choices=[
                    ("DS_JIRA", "Data Science Jira Ticket"),
                    ("DESIGN_DOC", "Experiment Design Document"),
                    ("ENG_TICKET", "Engineering Ticket (Bugzilla/Jira/GitHub)"),
                    ("QA_TICKET", "QA Testing Ticket (Bugzilla/Jira/Github)"),
                ],
                max_length=255,
            ),
        ),
    ]
