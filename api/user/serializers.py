from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField()

	def validate(self, data):
			email = data.get('email')
			password = data.get('password')

			if email and password:
				user = authenticate(email=email, password=password)

				if user:
					data['user'] = user  # Add validated user to serializer data
					return data
				else:
					raise ValidationError('Invalid email or password')
			else:
				raise ValidationError('Both email and password are required')


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('email', 'username')