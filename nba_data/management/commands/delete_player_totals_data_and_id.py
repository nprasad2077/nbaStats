from django.core.management.base import BaseCommand
from nba_data.models import PlayerTotalsData
from django.db import connection

class Command(BaseCommand):
    # Provides a description for use with the custom django management command (python manage.py help).
    help = 'Delete all player TOTALS data and reset primary key sequence in DB' 
    
    def handle(self, *args, **options):
        # Delete all player data
        PlayerTotalsData.objects.all().delete()
        
        # Reset the PK sequence
        with connection.cursor() as cursor:
            cursor.execute('ALTER SEQUENCE nba_data_playertotalsdata_id_seq RESTART WITH 1;')
        
        self.stdout.write(self.style.SUCCESS('Successfully deleted all players in DB'))