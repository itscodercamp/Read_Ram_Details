
from django.urls import path
from . import views

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('events/', views.events_view, name='events'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail_view, name='blog_detail'),  # Add this line for individual blog post
    path('contact/', views.contact_view, name='contact'),
    path('buymeacoffee/', views.buy_me_a_coffee_view, name='buymeacoffee'),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
