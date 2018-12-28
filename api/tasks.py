import csv
import logging
from os import path

from django.conf import settings

from demo.celery import app
from api.models import Institution

log = logging.getLogger(__name__)


@app.task(name='api.import_ipeds', bind=True)
def import_data(self, filename):
    data_file = path.join(settings.BASE_DIR, 'data', filename)
    with open(data_file, 'r', encoding = "latin-1") as f:
        csv_data = csv.reader(f, delimiter=',', dialect=csv.excel)
        next(csv_data, None)
        
        records = []
        
        for row in csv_data:
            ipeds_id, name, address, city, state,zip_code, fips = row[:7]
            record = Institution(ipeds_id=ipeds_id, name=name, address=address, city=city, state=state,
                                 zip_code=zip_code, FIPS=fips)
            records.append(record)
        
        log.info(f'Writing [{len(records)}] records to the db')
        Institution.objects.bulk_create(records)
