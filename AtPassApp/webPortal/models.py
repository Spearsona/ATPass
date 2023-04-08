from django.db import models

# Create your models here.
class AtUser(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dob = models.DateField('Date Of Birth')
    email = models.EmailField

    def __str__(self):
        return self.firstName + " " + self.lastName 

class Provider(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AtCategory(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    atcategory = models.ForeignKey(AtCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LoanInstance(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    atuser = models.ForeignKey(AtUser, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

