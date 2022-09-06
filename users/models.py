from django.db import models

class User (models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length = 100 , unique = True ,blank = False,default= " ")
    password = models.CharField(max_length = 100, blank = False,default= " ")
    first_name = models.CharField(max_length = 100, blank = True,default= " ")
    last_name = models.CharField(max_length = 100, blank = True,default= " ")
    email = models.CharField(max_length= 200, blank = True , default= " ",null=True)
    location = models.CharField(max_length=300,null = True ,blank = True)
    image =  models.IntegerField(null= True, blank= True)
    discraption = models.TextField(null = True)
    phonenumber = models.CharField(max_length = 15, blank = False, unique = True)
    isdoctor = models.BooleanField(default = False)

    class Meta:
      db_table = 'User'