from django.db import models
class Student(models.Model):
    #�ꏊ�̒萔
    ZAISITU = 0
    KYOSITU = 5
    KOUNAI = 10
    JITAKU = 15 
    
    #�o�Ȕԍ�
    number = models.IntegerField()
    #�ꏊ
    place = models.IntegerField()

# Create your models here.
