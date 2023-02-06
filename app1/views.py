"""
This file is used for writing business logic
"""


from django.shortcuts import render

# Create your views here.


def post_list(request):
    return render(request, "app1/app1_landing_page.html", {})


def welcome(request):
    return render(request, "app1/welcome.html")