from django.shortcuts import render
from django.http import JsonResponse

def list(request):
    list = [i for i in range(10)]
    return JsonResponse(list, safe=False)