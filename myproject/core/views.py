from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def users(request):
    users = User.objects.all()
    data = [{'username': user.username, 'email': user.email} for user in users]
    return JsonResponse({'data': data})
