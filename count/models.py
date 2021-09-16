from django.db import models
from django.conf import settings
from account.models import User

ROOM_CHOICES=(
    ('4a','전자정보실'),
    ('4b','미래열람실'),
    ('3a','문헌정보실'),
    ('3b','스터디실'),
    ('3c','시청각실'),
    ('2a','안내데스크'),
    ('2b','어린이실'),
    ('2c','북카페'),
    ('2d','장애인실'),
    ('2e','지혜열람실'),
    ('1a','식당/매점'),
    ('1b','문화교실'),
    ('pk','주차장'),
    ('etc','기타'),
)
# Create your models here.
class Count(models.Model):
    #1. 통계 정보에 대한 id 값
    id=models.BigAutoField(primary_key=True,blank=False,null=False)
    #2. 장소
    place=models.CharField(max_length=100,choices=ROOM_CHOICES)
    #3. 등록인
    user=models.ForeignKey(User,null=True, blank=True,on_delete=models.SET_NULL)
    #4. 해당 날짜
    when = models.DateField(blank=False,null=False)
    
    
    def __str__(self):
        tmadssa=''
        for rc in ROOM_CHOICES:
            if rc[0]==self.place:
                tmadssa=rc[1]
        return tmadssa+' '+self.when.strftime('%Y-%m-%d')
    
    
class Section(models.Model):
    #1. Section 고유 ID
    id=models.AutoField(primary_key=True,blank=False,null=False)
    #2. Section에 연결된 Count 외래 키
    count=models.ForeignKey(Count,null=False,blank=False,on_delete=models.CASCADE)
    #3. Section을 만든 유저
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    #4&5. Section의 각각 남여 숫자
    male=models.IntegerField(default=0)
    female=models.IntegerField(default=0)
    #6. Section 이름
    name=models.CharField(max_length=100,default='')
    
    def __str__(self):
        return self.name
    