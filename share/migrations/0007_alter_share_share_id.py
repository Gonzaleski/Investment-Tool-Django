# Generated by Django 4.2.11 on 2024-04-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0006_alter_share_share_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='share_id',
            field=models.AutoField(db_index=True, primary_key=True, serialize=False),
        ),
    ]
