from django.core.management.base import BaseCommand

from api.tasks import import_data


class Command(BaseCommand):
    help = "Imports ipeds data"
    ipeds_file = "hd2015.csv"
    
    def handle(self, *args, **options):
        import_data.apply_async([self.ipeds_file])
