from django.urls import path
from . import views 
from .views import home, about


urlpatterns = [
    # path('coin/', views.gen_coins, name='gen_coins'),
    # path('dice/', views.gen_dice, name='gen_dice'),
    # path('numb/', views.gen_number, name='gen_number'),
    path('', home, name='home'),
    path('about/', about, name='about')
]