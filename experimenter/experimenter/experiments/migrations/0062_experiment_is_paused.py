# Generated by Django 2.1.10 on 2019-07-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("experiments", "0061_auto_20190719_1540")]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="is_paused",
            field=models.BooleanField(default=False),
        )
    ]
