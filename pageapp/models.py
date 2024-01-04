from django.db import models

class passList(models.Model):
    username = models.CharField(max_length= 25,unique = False)
    usernum  = models.IntegerField(unique = True)


class userList(models.Model):
    username = models.CharField(max_length= 25,unique = False)
    usernum  = models.IntegerField(unique = True)


# Create your models here.
