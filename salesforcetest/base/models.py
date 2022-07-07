from tkinter import CASCADE
from django.db import models
from salesforce.models import *
import salesforce
# Create your models here.


class Account(salesforce.models.Model):
   
    Name= models.CharField(max_length=200)


    def __str__(self):
         return self.Name
    




class User(salesforce.models.Model):
   
    Name= models.CharField(max_length=200)
    
    
    def __str__(self):
         return self.Name



class Opportunity(salesforce.models.Model):
    
    Name= models.CharField(max_length=200)
    Amount= models.CharField(max_length=200)
    AccountId = models.ForeignKey(Account, db_column='AccountId', on_delete=models.CASCADE)
    OwnerId = models.ForeignKey(User , on_delete=models.CASCADE   ,db_column='OwnerId')


    def __str__(self):
         return self.Name