from rest_framework import serializers
from authentication.models import MyUser


class Regsiterserializer(serializers.ModelSerializer):
    password =serializers.CharField(max_length=128, write_only=True)
    class Meta:
        model = MyUser
        fields = ('username','email','first_name', 'last_name', 'password')
        
        
        
    def creat(self, **validated_data):
        return MyUser.objects.create(**validated_data)