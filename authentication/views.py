
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import Regsiterserializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate



class RegsiterAPIView(GenericAPIView):
    serializer_class= Regsiterserializer
    
    def post(self, request):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
class LoginAPIView(GenericAPIView):
    
    serializer_class= LoginSerializer
    def post (self, request):
        email = request.data.get('email', None)
        password = request.data.get('password',None)
        
        user = authenticate(username=email, password=password)
        
        
        if user:
            serializer= self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': "Invalid credentials try again"}, status= status.HTTP_401_UNAUTHORIZED)
        