from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterUserSerializer,LoginUserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from django.contrib.auth.models import User

# Create your views here.

class Home(APIView):
    def get(self,request):
        return Response({"msg":"hello world"})
    

class RegisterUser(APIView):
    def post(self,request):
        serializer = RegisterUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        user = serializer.create(serializer.validated_data)
        user = RegisterUserSerializer(user)
        return Response(user.data)
        # return Response({"msg":"user account created successfully"})
    

class LoginUser(APIView):
    def post(self,request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user=user)
            return Response({"refresh":str(refresh), "access": str(refresh.access_token)})
        else:
            return Response({"error": "Invalid Credentials"})
        

class GetUsersData(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        users = request.user
        serializer = LoginUserSerializer(users)
        return Response(serializer.data)


