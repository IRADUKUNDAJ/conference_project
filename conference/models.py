from calendar import day_abbr, day_name
from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MaxLengthValidator
import datetime

# Create your models here.
class conference(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=380, blank=True, null=False)
    dates=models.DateField()
    location=models.TextField(max_length=380, blank=True, null=False)
    topics= models.TextField(max_length=380, blank=True, null=False)

   

