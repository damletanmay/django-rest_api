from django.db import models
from django.contrib.auth.models import User

# advisor model to store all advisors.
class Advisor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default = None,max_length = 30)
    img_url = models.TextField(default = None)

    def __str__(self):
        return str(self.id)

# bookings model to store what user has booked what advisor
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    advisor_id = models.ForeignKey(Advisor,on_delete = models.CASCADE,default=None)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE,default=None)
    # added advisor id & user id as a foreign key, to avoid data redundancy.
    time = models.CharField(default = None,max_length = 50)

    def __str__(self):
        return str(self.id)
