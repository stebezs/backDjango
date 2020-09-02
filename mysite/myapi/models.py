from django.db import models

# Create your models here.
class Launch(models.Model):
    
    launch_year = models.IntegerField()
    launch_date_utc = models.CharField(max_length = 100)
    launch_date_local = models.CharField(max_length = 100)
    rocket_id = models.CharField(max_length = 100)
    rocket_name = models.CharField(max_length = 100)
    rocket_type = models.CharField(max_length = 100)
    land_success = models.CharField(max_length=50)
    site_name = models.CharField(max_length = 100)
    customer = models.CharField(max_length = 100)
    nationality = models.CharField(max_length = 100)
                
    launch_success = models.CharField(max_length=50)

    def as_json(self):
        return dict (
            launch_year = self.launch_year,
            launch_date_utc = self.launch_date_utc,
            launch_date_local = self.launch_date_local,
            rocket_id = self.rocket_id,
            rocket_name = self.rocket_name,
            rocket_type = self.rocket_type,
            land_success = self.land_success,
            site_name = self.site_name,
            customer = self.customer,
            nationality = self.nationality,
            launch_success = self.launch_success

        )
