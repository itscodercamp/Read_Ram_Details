from django.urls import path

from . import views

urlpatterns = [
    path('/login/',views.login,name='login'),
    path('/signup/',views.signup,name='signup'),

]

from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 