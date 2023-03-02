# Generated by Django 4.1.7 on 2023-03-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0006_rename_type_issue_type_old"),
    ]

    operations = [
        migrations.AddField(
            model_name="issue",
            name="type",
            field=models.ManyToManyField(
                blank=True, related_name="issue_set", to="webapp.type"
            ),
        ),
    ]