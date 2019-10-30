from django.urls import path
from . import views
urlpatterns = [

path('',views.home,name='home'),
    path('prices/',views.prices,name='prices'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup')

]