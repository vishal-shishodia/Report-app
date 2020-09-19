from django.urls import path,include

from .views import*
app_name='app'


urlpatterns = [
    path('',home,name='home'),
    path('index/',index,name='index'),
    path('register/',SignUp,name='register'),
    path('createreport/',CreateReport,name='createreport'),
    path('login/',UserLogin,name='login'),
    path('logout/',Logout,name='logout'),

]