from rest_framework import serializers
from .models import *
import datetime
class CountSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Count
        fields = ['id','place','user','when']
        
class TodayCountSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    when = serializers.ReadOnlyField(source = datetime.datetime.now().date().strftime('%Y-%m-%d'))
    class Meta:
        model = Count
        fields = ['id','place','user','when']        
        
class SectionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Section
        fields = ['id','count','user','male','female','name']
        
class TodaySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    count=serializers.PrimaryKeyRelatedField(queryset=Count.objects.filter(when=datetime.datetime.now().date()))
    
    class Meta:
        model=Section
        fields=['id','count','user','male','female','name'] 