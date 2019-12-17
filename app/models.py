from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.
#user model already has the fields for username, password, first name, last name etc...
class UserModel(User):
    location = models.CharField(max_length=100, blank = True)
    date_of_birth = models.DateField(blank=False)
    def __str__(self):
        return self.username

class Items(models.Model):
    seller = models.ForeignKey(UserModel, on_delete= models.CASCADE, related_name='bidder')
    itemImage = models.ImageField(upload_to = 'pic_folder/', null=True, blank=True)
    itemName = models.CharField(max_length = 50)
    itemDescription = models.CharField(max_length = 500)
    itemAdded = models.DateField(("Date"), default=datetime.date.today)
    itemAuctonEnd = models.DateField()
    itemPrice = models.DecimalField(max_digits=8, decimal_places=2)
    highestBidder = models.CharField(max_length=50, blank = True)
    bidderList = models.CharField(max_length=5000, blank = True)
    def __str__(self):
        return self.itemName



