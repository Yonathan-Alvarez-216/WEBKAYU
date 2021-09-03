from django.urls import path
from .views import *


urlpatterns = [
    path('', astra, name='astra'),
    path('astra2/', astra2, name='astra2'),
]

