# your_app/management/commands/update_daily_price.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from share.models import Share, MinMax, DailyPrice
from datetime import datetime
import pytse_client as tse

class Command(BaseCommand):
    help = "Fetch and update today's stock data into the database"

    def handle(self, *args, **kwargs):
        today = datetime.today().date()

        # Fetch today's data for each share
        shares = Share.objects.all()
        for share in shares:
            try:
                ticker = tse.Ticker(share.symbol)
                last_date = ticker.last_date.date()
            except Exception as e:
                self.stderr.write(f"Error fetching ticker or last date for {share.symbol}: {e}")
                continue

            if last_date != today:
                self.stdout.write(f"No data available for {share.symbol} for today.")
                continue

            try:
                share_price, created = MinMax.objects.get_or_create(
                    share=share,
                    date=today,
                    defaults={
                        'date': today,
                        'max': int(ticker.high_price),
                        'min': int(ticker.low_price),
                    }
                )

                if created:
                    self.stdout.write(f"Added today's data for {share.symbol}")
                else:
                    self.stdout.write(f"Today's data for {share.symbol} already exists")
            except Exception as e:
                self.stderr.write(f"Error saving data for {share.symbol}: {e}")
                continue

        # Update DailyPrice for each user
        # users = User.objects.all()
        # for user in users:
        #     try:
        #         daily_price, created = DailyPrice.objects.get_or_create(
        #             user=user,
        #             date=today,
        #             defaults={
        #                 'gold_price': 0,  # You need to fetch the actual gold price
        #                 'dollar_price': 0,  # You need to fetch the actual dollar price
        #             }
        #         )
        #         if created:
        #             self.stdout.write(f"Added today's daily price for {user.username}")
        #         else:
        #             self.stdout.write(f"Today's daily price for {user.username} already exists")
        #     except Exception as e:
        #         self.stderr.write(f"Error updating daily price for {user.username}: {e}")
        #         continue
