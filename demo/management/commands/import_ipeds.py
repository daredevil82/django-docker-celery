import csv
from os import path

from django.conf import settings
from django.core.management.base import BaseCommand

from api.models import Institution


class Command(BaseCommand):
    help = "Imports ipeds data"
    ipeds_file = "hd2015.csv"
    
    def handle(self, *args, **options):
        data_file = path.join(settings.BASE_DIR, 'data', self.ipeds_file)
        with open(data_file, 'r', encoding = "latin-1") as f:
            csv_data = csv.reader(f, delimiter=',', dialect=csv.excel)
            next(csv_data, None)
            
            records = []
            
            for row in csv_data:
                ipeds_id, name, address, city, state,zip_code, fips = row[:7]
                record = Institution(ipeds_id=ipeds_id, name=name, address=address, city=city, state=state,
                                     zip_code=zip_code, FIPS=fips)
                records.append(record)
            
            self.stdout.write(f'Writing [{len(records)}] records to the db')
            Institution.objects.bulk_create(records)
