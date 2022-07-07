from django.urls import path
from . import views


urlpatterns = [
    path("home/" , views.home),
    path("Orders/" , views.order),
    # path("Accounts/",views.account),
    # path("Users/",views.user),



]