from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='home'),
# home page area
path('Dashboard/', views.Dashboard,name='dashboard'),

# registration login and logout urls area
path('login/', views.Login,name='login'),
path('Registration/', views.Regester,name='regester'),

# CheckRegistration area
path('CheckRegistration/', views.CheckRegistration,name='CheckRegistration'),
# loginCheck area
path('loginCheck/', views.loginCheck,name='loginCheck'),
# logout url
path('Logout/', views.LogOut,name='logout'),
]




from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 