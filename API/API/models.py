from django.db import models

class an_asigned_truck(models.Model):
    number_plate = models.CharField(max_length=50, default='no truck assigned')

    def __str__(self):
        return f"{self.number_plate}"

class City(models.Model):
    city_name = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f"{self.city_name}"

class District(models.Model):
    district_name = models.CharField(max_length=100, null=True)
    citys = models.ForeignKey(City, on_delete = models.PROTECT)
    
    def __str__(self):
        return f"{self.district_name}"

languages = [
        ('BM', 'BM'),
        ('BI', 'BI'),
        ('BC', 'BC')
        ]

class Driver(models.Model):    
    name = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    email = models.EmailField()
    language = models.CharField(max_length=100, choices=languages, default='BM')
    truck = models.ManyToManyField(an_asigned_truck, related_name='trucks')
    city_district = models.ForeignKey(City, on_delete = models.PROTECT, related_name='citys')

    def __str__(self):
        return f"{self.name}"

# py manage.py makemigrations
# py manage.py migrate
# py manage.py runserver
# py manage.py flush
# py manage.py createsuperuser