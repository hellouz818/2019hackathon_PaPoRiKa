from django.db import models
#from django.contrib.auth import get_user_model
# Create your models here.

class Market(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    #summary = models.CharField(null=True, max_length=100)
    body = models.TextField(default='')
    #image = models.ImageField(null=True, upload_to='images/')
    pptfile = models.FileField(null=True, upload_to='documents/')

    def __str__(self):
        return self.title