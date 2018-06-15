from django.db import models
class Student(models.Model):
    #êŠ‚Ì’è”
    ZAISITU = 0
    KYOSITU = 5
    KOUNAI = 10
    JITAKU = 15 
    
    #oÈ”Ô†
    number = models.IntegerField()
    #êŠ
    place = models.IntegerField()

# Create your models here.
