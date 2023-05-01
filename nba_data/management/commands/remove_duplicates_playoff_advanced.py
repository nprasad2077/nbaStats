from django.core.management.base import BaseCommand
from nba_data.models import PlayerPlayoffAdvancedData


class Command(BaseCommand):
    help = 'Remove duplicate records for DAL and BOS in season 2010'

    def handle(self, *args, **options):
        season = 2010
        teams = ['DAL', 'BOS']

        for team in teams:
            duplicates = PlayerPlayoffAdvancedData.objects.filter(season=season, team=team).order_by('player_name')

            # Group records by name
            players_grouped = {}
            for duplicate in duplicates:
                if duplicate.player_name not in players_grouped:
                    players_grouped[duplicate.player_name] = []
                players_grouped[duplicate.player_name].append(duplicate)

            # Delete duplicates while keeping one record per player
            for player_name, player_records in players_grouped.items():
                if len(player_records) > 1:
                    for player_record in player_records[1:]:
                        player_record.delete()
                        self.stdout.write(self.style.SUCCESS(f"Deleted duplicate {player_name} for {team} in season {season}"))