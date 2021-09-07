from django.db import models
from django.db.models.fields.json import JSONField

# Create your models here.
def jsonfield_default():
    return {
        '안내데스크':False,
        '어린이실':False,
        '북카페':False,
        '미래열람실':False,
        '장애인실':False,
        '시청각실':False,
        '스터디룸':False,
        '문헌정보실':False,
        '지혜열람실':False,
        '전자정보실':False,
        '문화교실':False,
        '식당':False,
        '기타':False,
    }


class PersonModel(models.Model):
    name=models.CharField(max_length=50)
    kolasid=models.CharField(max_length=70)
    count=models.IntegerField()
    places=models.JSONField(default=jsonfield_default)
    detail=models.TextField()
    
    def __str__(self):
        return self.name if self.name is not None else self.kolasid
    def key(self):
        return ['name', 'kolasid', 'count', 'places','detail']