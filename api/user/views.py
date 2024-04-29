from django.contrib.auth import login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserLoginSerializer, UserSerializer
from rest_framework import permissions, status
from ..validations import custom_validation, validate_email, validate_password
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class UserRegister(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            if created:
                return Response({'message': 'User created successfully', 'token': token.key}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'User already exists', 'token': token.key}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""Login"""
from django.contrib.auth import authenticate


class LoginUser(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']  # Retrieve validated user from serializer
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = UserSerializer(user)
            return Response({
                'message': 'Login successful',
                'success': True,
                'token': token.key,
                'user': user_serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	##
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)