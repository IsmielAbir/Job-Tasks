from django.urls import path
from assets.views import test
urlpatterns = [
    path('', test),
    
]
