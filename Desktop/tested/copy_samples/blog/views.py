from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from .models import BlogPost, Contact

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def events_view(request):
    return render(request, 'events.html')

def blog_view(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def blog_detail_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_detail.html', {'post': post})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, number=number, email=email, message=message)
        contact.save()

        return JsonResponse({'success': True})
    return render(request, 'contact.html')

def buy_me_a_coffee_view(request):
    return render(request, 'buymeacoffee.html')
