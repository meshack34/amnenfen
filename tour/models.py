#tour/models
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


# class Destination(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinations')
#     name = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     description = models.TextField()
#     map_embed_code = models.TextField(help_text="Embed iframe from Google Maps")
    
#     def get_valid_dates(self):
#         valid_dates = []
#         for date_range in self.date_ranges.all():
#             current = date_range.start_date
#             while current <= date_range.end_date:
#                 valid_dates.append(current)
#                 current += timedelta(days=1)
#         return valid_dates
    
#     def __str__(self):
#         return self.name
    
# tour/models.py
class Destination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinations')
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    map_embed_code = models.TextField(help_text="Embed iframe from Google Maps")

    def get_valid_dates(self):
        from datetime import timedelta
        valid_dates = []
        for date_range in self.date_ranges.all():
            current = date_range.start_date
            while current <= date_range.end_date:
                valid_dates.append(current)
                current += timedelta(days=1)
        return valid_dates

    def __str__(self):
        return self.name


class DateRange(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='date_ranges')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.destination.name}: {self.start_date} to {self.end_date}"




class DestinationImage(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='destination_gallery/')

class Room(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='rooms/')
    cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Cost per night in KSh")
    basis = models.CharField(max_length=50, help_text="e.g., FB, HB, BB")
    nights = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name} ({self.destination.name})"


class Restaurant(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='restaurants/')

class Activity(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.title} on {self.date} from {self.start_time} to {self.end_time}"



class Information(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='info')
    content = models.TextField()
