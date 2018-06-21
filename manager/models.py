from django.db import models
class Student(models.Model):

    ZAISITU = "在室"
    KYOSITU = "教室"  
    KOUNAI = "校内"
    JITAKU = "自宅"

    PLACE_CHOICES = (
            ("在室", '在室'),
            ("教室", '教室'),
            ("校内", '校内'),
            ("自宅", '自宅'),
    )
    
    number = models.IntegerField()
    place = models.CharField(max_length=2, choices=PLACE_CHOICES, default = None)

# Create your models here.
