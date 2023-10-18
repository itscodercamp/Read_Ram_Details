
from django.urls import path
from . import views

urlpatterns = [
    # Add your app URL patterns here
    path('', views.HOME, name='home'),

    path('add', views.Add, name='add'),

    path('edit/<int:id>/', views.edit_form, name='edit_form'),
    path('edits/', views.edit, name='edit'),
    path('delete/', views.Delete, name='delete'),
    

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
