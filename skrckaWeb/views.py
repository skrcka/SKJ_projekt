from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect


def index(request):
    return redirect('/shop')
