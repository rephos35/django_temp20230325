from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions
# from rest_framework.views import APIView
# from rest_framework.authtoken.models import Token


from account.models import AccountModel
from account.serializers import AccountSerializer
from account.utils import verify_recaptcha

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
# authentication_class = [JWTAuthentication]


@api_view(['POST'])
def signup_view(request): 
    # recaptcha_token = request.data.get('g-recaptcha-response')
    # if not verify_recaptcha(recaptcha_token):
    #     json_response = {'status': 'error', 'message': 'reCAPTHCHA verification failed'}
    #     return Response(json_response, status=status.HTTP_401_UNAUTHORIZED)
    
    serializer = AccountSerializer(data=request.data)
    if not serializer.is_valid():
        json_response = {'status': 'error', 'message': serializer.errors}
        return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
    
    # = serializer def create(self, validated_data)
    user = serializer.save()
    user.set_password(user.password)
    user.save()

    json_response = {
        'status': 'success',
        'message': 'signup successfully',
    }
    return Response(json_response, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def login_view(request):
    # recaptcha_token = request.data.get('g-recaptcha-response') 
    # if not verify_recaptcha(recaptcha_token):
    #     json_response = {'status': 'error', 'message': 'reCAPTHCHA verification failed'}
    #     return Response(json_response, status=status.HTTP_401_UNAUTHORIZED)
    
    # permission_classes = [permissions.AllowAny]
    # get data
    account = request.data.get('account') # POST[''] # POST.get
    password = request.data.get('password')
    user = authenticate(request, account=account, password=password)
    if user is None:
        json_response = {'status': 'error', 'message': 'Invalid username or password'}
        return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
    
    # login
    login(request, user)
    # generate simpletoken
    # jwt_token = {
    #     'access_token': str(AccessToken.for_user(user)),
    #     'refresh_token': str(RefreshToken.for_user(user))
    # }
    json_response = {
        'status': 'success',
        'message': 'login successfully',
        'user': {
            'account': user.account,
            'is_superuser': user.is_superuser,
        },
        # 'jwt_token': jwt_token
    }
    # create token
    # token, created = Token.objects.get_or_create(user=user)
    # json_data = {'token': token.key}
    return Response(json_response, status=status.HTTP_200_OK)



@api_view(['POST'])
def logout_view(request):
    # delete token
    # request.user.auth_token.delete()
    # request.user.jwt_token.delete()
    

    # refresh_token = request.data.get('refresh_token')
    # token = RefreshToken(refresh_token)
    # token.blacklist()
    # logout
    logout(request) # clean auth session data
    json_response = {'status': 'success'}
    return Response(json_response, status=status.HTTP_200_OK)



