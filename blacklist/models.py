from django.db import models
from django.db.models.fields import DateField

PLACE_NAME=['전자정보실','미래열람실','컴퓨터교육실','문헌정보실','스터디룸','시청각실','안내데스크','어린이실','지혜열람실','북카페','장애인실','식당/매점','문화교실','로비/복도','주차장','기타']

# Create your models here.
class Person(models.Model):
    no=models.AutoField(primary_key=True,default=1,unique=True)
    name=models.CharField(max_length=40)
    kolasid=models.CharField(max_length=50)
    count=models.IntegerField(default=1)
    places={}
    for name in PLACE_NAME:
        places[name]=models.BooleanField(default=False)
    detail=models.TextField(blank=True)
    first=models.DateField(auto_now_add=True)
    recent=models.DateField(auto_now=True)
    image=models.ImageField(null=True, blank=True)
    file=models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.name if self.name!=None else self.kolasid
    
    def keys():
        return ['no','name','kolasid','count','places','detail','first','recent','image','file']