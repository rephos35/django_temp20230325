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
def register_view(request): 
    recaptcha_token = request.data.get('recaptcha_token')
    if verify_recaptcha(recaptcha_token):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            # = serializer def create(self, validated_data)
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            # return JsonResponse({"status": "success"})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse({"status": "failed", "error": "Invalid username or password"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return JsonResponse({"status": "failed", "error": "reCAPTCHA verification failed"})
    return Response({'detail': 'reCAPTCHA verification failed'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def login_view(request):
    recaptcha_token = request.data.get('recaptcha_token') # POST.get
    if verify_recaptcha(recaptcha_token):
        # permission_classes = [permissions.AllowAny]
        # get data
        account = request.data.get('account') # POST['']
        password = request.data.get('password')
        user = authenticate(request, account=account, password=password)
        if user is not None:
            # login
            login(request, user)
            # simpletoken
            jwt_token = {
                'access_token': str(access_token = AccessToken.for_user(user)),
                'refresh_token': str(refresh_token = RefreshToken.for_user(user)),
            }


            # create token
            ## token, created = Token.objects.get_or_create(user=user)
            ## return Response({'token': token.key}, status=status.HTTP_200_OK)
            # return JsonResponse({"status": "success"})
            # return Response({'detail': 'Logged in successfully'}, status=status.HTTP_200_OK)
            return Response(jwt_token, status=status.HTTP_200_OK)
        ## return Response({'error': 'Invalid login credentials'}, status=status.HTTP_400_BAD_REQUEST)
        # return JsonResponse({"status": "failed", "error": "Invalid username or password"})
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    # return JsonResponse({"status": "failed", "error": "reCAPTCHA verification failed"})
    return Response({'detail': 'reCAPTCHA verification failed'}, status=status.HTTP_401_UNAUTHORIZED)
















@api_view(['POST'])
def logout_view(request):
    # delete token
    # request.user.auth_token.delete()
    # logout
    logout(request)
    return Response({'detail':'Logged out successfully'}, status=status.HTTP_200_OK)



