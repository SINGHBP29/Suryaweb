from django.db import models
class signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.IntegerField(max_length=20, blank=True)
# Create your models here.
