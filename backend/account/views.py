from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from account.models import AccountModel
from account.serializers import AccountSerializer

# def test(request):
#     account = AccountModel.objects.all()
#     return HttpResponse(account)

# def account_login(request):
#     json_data = {'status': 'success'}
#     return JsonResponse(json_data)

# class ListProject(generics.ListCreateAPIView):
#     querset = AccountModel.all()
#     serializer_class = AccountSerializer


# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer


def cookie_view(request):
    response = HttpResponse('Set your lucky_number as 8')
    response.set_cookie = ('lucky_number', 8)
    return response

@api_view(['POST'])
def register_view(request): 
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    account = request.data.get('account')
    password = request.data.get('password')
    user = authenticate(request, account=account, password=password)
    if user is not None:
        login(request, user)
        return Response({'detail': 'Logged in successfully'}, status=status.HTTP_200_OK)
    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'detail':'Logged out successfully'}, status=status.HTTP_200_OK)


# class LoginView(View):
#     def get(self, request):
#         json_data = {}
#         return JsonResponse(json_data)
#     def post():
#         pass 

# class LoginView(View):
#     template_name = '.html'

#     def get(self, request):
#         return render(request, self.template_name)
#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, self.template_name, {'error_message': 'Invalid login'})

# class MyView(View):
#     template_name = 'my_template.html'

#     def get(self, request):
#         return render(request, self.template_name)
    
# class GreetingView(View):
#     greeting = "Good Day"

#     def get(self, request):
#         return HttpResponse(self.greeting)
    
