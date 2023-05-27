from django.db import models

# Create your models here.
class Contact(models.Model):
   
    email=models.CharField(max_length=50,null=True)
    name=models.CharField( max_length=50,null=True)
    phone=models.CharField( max_length=50,null=True)
    desc=models.TextField(null=True)
    date=models.DateField() 
    def __str__(self):
        return str(self.name)

 