from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    '''
    Show 'Hello bookstore!' in the main page
    '''
    return HttpResponse('Hello bookstore!')

# Create your views here.
