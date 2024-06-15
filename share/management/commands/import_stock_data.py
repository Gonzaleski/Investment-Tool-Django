# your_app/management/commands/import_stock_data.py
import os
import csv
from django.core.management.base import BaseCommand
from share.models import Share, SharePrice
from datetime import datetime

class Command(BaseCommand):
    help = 'Import stock data from CSV files into the database'

    def add_arguments(self, parser):
        parser.add_argument('folder_path', type=str, help='Path to the folder containing CSV files')

    def handle(self, *args, **kwargs):
        folder_path = kwargs['folder_path']
        for filename in os.listdir(folder_path):
            if filename.endswith('.csv'):
                symbol = os.path.splitext(filename)[0]
                self.stdout.write(f"Processing {symbol}...")

                # Get or create the Share object
                share, created = Share.objects.get_or_create(symbol=symbol)

                with open(os.path.join(folder_path, filename), 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        date = datetime.strptime(row['date'], '%Y-%m-%d').date()

                        # Only update or create if the record doesn't already exist
                        if not SharePrice.objects.filter(share=share, date=date).exists():
                            SharePrice.objects.create(
                                share=share,
                                date=date,
                                open=float(row['open']),
                                high=float(row['high']),
                                low=float(row['low']),
                                adj_close=float(row['adjClose']),
                                value=int(row['value']),
                                volume=int(row['volume']),
                                count=int(row['count']),
                                yesterday=float(row['yesterday']),
                                close=float(row['close']),
                            )

                self.stdout.write(f"Completed {symbol}")

