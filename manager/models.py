from django.db import models
class Student(models.Model):
    #場所の定数
    ZAISITU = 0
    KYOSITU = 5
    KOUNAI = 10
    JITAKU = 15 
    
    #出席番号
    number = models.IntegerField()
    #場所
    place = models.IntegerField()

# Create your models here.
