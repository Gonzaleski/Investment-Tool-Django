# Generated by Django 4.2.11 on 2024-04-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell_share', '0009_rename_share_id_sellshare_share_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellshare',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
