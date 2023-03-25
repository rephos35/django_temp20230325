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

def test(request):
    account = AccountModel.objects.all()
    return HttpResponse(account)

def account_login(request):
    json_data = {'status': 'success'}
    return JsonResponse(json_data)

class ListProject(generics.ListCreateAPIView):
    querset = AccountModel.all()
    serializer_class = AccountSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


def cookie_view(request):
    response = HttpResponse('Set your lucky_number as 8')
    response.set_cookie = ('lucky_number', 8)
    return response







class LoginView(View):
    def get(self, request):
        json_data = {}
        return JsonResponse(json_data)
    def post():
        pass 

class LoginView(View):
    template_name = '.html'

    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, self.template_name, {'error_message': 'Invalid login'})

class MyView(View):
    template_name = 'my_template.html'

    def get(self, request):
        return render(request, self.template_name)
    
class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)
    


# v2
    # captcha_key = request.data.get('captcha_key')
    # captcha_value = request.data.get('captcha')

    
    # recaptcha_response = request.data.get('g-recaptcha-response')
    # # Verify reCAPTCHA
    # recaptcha_verification_url = 'https://www.google.com/recaptcha/api/siteverify'
    # recaptcha_data = {
    #     'secret': settings.RECAPTCHA_PRIVATE_KEY,
    #     'response': recaptcha_response
    # }
    # recaptcha_result = requests.post(recaptcha_verification_url, data=recaptcha_data)
    # recaptcha_success = recaptcha_result.json().get('success')

    # if not recaptcha_success:
    #     return Response({'error': 'Invalid reCAPTCHA'}, status=status.HTTP_400_BAD_REQUEST)
