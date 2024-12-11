from django.db import models

# Create your models here.
class com(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Type = models.CharField(max_length=100)

class adm(models.Model):
    LoginId = models.ForeignKey(com, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class man(models.Model):
    LoginId = models.ForeignKey(com, on_delete=models.CASCADE, null=True)
    Name= models.CharField(max_length=100)
    Email = models.EmailField()
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class emp(models.Model):
    LoginId = models.ForeignKey(com, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)

    def __str__(self):
        return self.Name