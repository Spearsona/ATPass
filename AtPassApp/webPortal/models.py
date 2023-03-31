from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dob = models.DateField('Date Of Birth')
    email = models.EmailField

class Provider(models.Model):
    name = models.CharField(max_length=100)

class AtCategory(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    atcategory = models.ForeignKey(AtCategory, on_delete=models.CASCADE)


class Loan(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)