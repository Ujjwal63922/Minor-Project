from django.db import models

class userform(models.Model):
    CHOICES=[
        ('Plot','Plot'),
        ('Flat','Flat'),
        ('Farm House','Farm House'),
    ]
    name = models.CharField(max_length=40)
    email = models.EmailField()
    contact = models.PositiveBigIntegerField()
    category = models.CharField(max_length=15,choices=CHOICES)
    location = models.CharField(max_length=40)
    price  = models.PositiveBigIntegerField()
    description = models.TextField()
    status=models.CharField(max_length=12,null=True)
    
class contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    description = models.TextField()
    
class buy_form(models.Model):
    p_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.PositiveBigIntegerField()