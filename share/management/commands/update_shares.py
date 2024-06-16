# management/commands/update_shares.py

import pytse_client as tse
from django.core.management.base import BaseCommand
from share.models import Share

class Command(BaseCommand):
    help = 'Updates the title and group of shares using the pytse-client library.'

    def handle(self, *args, **kwargs):
        shares = Share.objects.all()
        for share in shares:
            try:
                print(type(share.symbol))
                ticker = tse.Ticker(share.symbol)
                if ticker:
                    if hasattr(ticker, 'title') and hasattr(ticker, 'group_name'):
                        share.title = ticker.title
                        share.group = ticker.group_name
                        share.save()
                        self.stdout.write(self.style.SUCCESS(f'Successfully updated {share.symbol}'))
                    else:
                        self.stdout.write(self.style.ERROR(f'Ticker attributes not found for {share.symbol}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Ticker not found for {share.symbol}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error updating {share.symbol}: {e}'))