# Generated by Django 4.2.11 on 2024-04-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell_share', '0004_alter_sellshare_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellshare',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
    ]
