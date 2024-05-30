from django.db import migrations, connection

def reset_transaction_id_sequence(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='transactions_transaction';")

class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_alter_transaction_dollar_price_and_more'),
    ]

    operations = [
        migrations.RunPython(reset_transaction_id_sequence),
    ]