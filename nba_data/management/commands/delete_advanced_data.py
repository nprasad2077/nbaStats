from django.core.management.base import BaseCommand
from nba_data.models import PlayerAdvancedData
from django.db import connection

class Command(BaseCommand):
    # Provides a description for use with the custom django management command (python manage.py help).
    help = 'Delete all player ADVANCED data with season specified and reset primary key sequence in DB' 
    
    def handle(self, *args, **options):
        # Delete player data with season
        season = 2006
        PlayerAdvancedData.objects.filter(season=season).delete()
        
        # Reset the PK sequence
        with connection.cursor() as cursor:
            cursor.execute('ALTER SEQUENCE nba_data_playeradvanceddata_id_seq RESTART WITH 1;')
        
        self.stdout.write(self.style.SUCCESS('Successfully deleted all players with season = {} in DB'.format(season)))