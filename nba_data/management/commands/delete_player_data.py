from django.core.management.base import BaseCommand
from nba_data.models import PlayerData

class Command(BaseCommand):
    # Provides a description for use with the custom django management command (python manage.py help).
    help = 'Delete all player data' 
    
    def handle(self, *args, **options):
        # Delete all player data
        PlayerData.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Successfully deleted all players in DB'))