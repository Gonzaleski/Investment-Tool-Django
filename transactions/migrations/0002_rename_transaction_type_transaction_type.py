# Generated by Django 4.2.11 on 2024-05-24 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction",
            old_name="transaction_type",
            new_name="type",
        ),
    ]