from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
#LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class FoodTruck(models.Model):
	
	objectid = models.IntegerField(primary_key=True)
	applicant = models.CharField(max_length=128, blank=True, null=True)
	facilitytype = models.CharField(max_length=64, default='Truck', blank=True, null=True)
	cnn = models.IntegerField(blank=True, null=True)
	locationdescription = models.CharField(max_length=512, blank=True, null=True)
	address = models.CharField(max_length=512, blank=True, null=True)
	blocklot = models.CharField(max_length=16, blank=True, null=True)
	block = models.CharField(max_length=16, blank=True, null=True)
	lot = models.CharField(max_length=16, blank=True, null=True)
	permit = models.CharField(max_length=16, blank=True, null=True)
	status = models.CharField(max_length=16, blank=True, null=True)
	fooditems = models.CharField(max_length=512, blank=True, null=True)
	x = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	y = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
	latitude = models.DecimalField(db_index=True, max_digits=15, decimal_places=12, blank=True, null=True)
	longitude = models.DecimalField(db_index=True, max_digits=15, decimal_places=12, blank=True, null=True)
	schedule = models.URLField(max_length=512, blank=True, null=True)
	noisent = models.DateTimeField(blank=True, null=True)
	approved = models.DateTimeField( blank=True, null=True)
	received = models.DateTimeField( blank=True, null=True)
	priorpermit = models.IntegerField(blank=True, null=True)
	expirationdate = models.DateTimeField( blank=True, null=True)
	#location = models.CharField(max_length=64, blank=True, null=True)

	class Meta:
		ordering = ('objectid',)