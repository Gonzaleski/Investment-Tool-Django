# Generated by Django 5.0.6 on 2024-05-31 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("share", "0009_dailyprice_user_alter_dailyprice_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyprice",
            name="date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="dailyprice",
            name="id",
            field=models.AutoField(db_index=True, primary_key=True, serialize=False),
        ),
    ]