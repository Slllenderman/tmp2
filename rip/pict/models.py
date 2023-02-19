from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    ROLES = [
        ('M', 'manager'),
        ('U', 'user')
    ]
    role = models.CharField(max_length=1, choices=ROLES)

class Pictures(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='./static/pict')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Orders(models.Model):
    creation = models.DateField()
    payment = models.DateField()
    delivery = models.DateField()
    STATES = [
        ('A', 'created'),
        ('B', 'paid'),
        ('C', 'delivered')
    ]
    status = models.CharField(max_length=1, choices=STATES)
    quantity = models.IntegerField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE)


