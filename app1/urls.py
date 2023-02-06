"""
<home-url>/myapp1/
<home-url>/myapp1/welcome
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list),
    path("welcome/", views.welcome)
]