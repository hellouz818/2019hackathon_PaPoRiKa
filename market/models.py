from django.db import models
#from django.contrib.auth import get_user_model
# Create your models here.

class Market(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(default='')
    pptfile = models.FileField(null=True, upload_to='documents/')

    def __str__(self):
        return self.title
