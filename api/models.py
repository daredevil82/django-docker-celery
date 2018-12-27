from django.db import models


class Institution(models.Model):
    ipeds_id = models.IntegerField(help_text = "IPEDS unique institution ID", unique = True)
    name = models.CharField(max_length = 150)
    address = models.CharField(max_length = 150)
    city = models.CharField(max_length = 40)
    state = models.CharField(max_length = 2)
    zip_code = models.CharField(max_length = 20)
    FIPS = models.IntegerField()
