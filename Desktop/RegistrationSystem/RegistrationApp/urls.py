from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='home'),

path('login/',views.login,name='login'),
path('signup/',views.signup,name='signup'),

path('login_check/',views.login_check,name='login_check'),
path('signup_check/',views.signup_check,name='signup_check'),

]




from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 