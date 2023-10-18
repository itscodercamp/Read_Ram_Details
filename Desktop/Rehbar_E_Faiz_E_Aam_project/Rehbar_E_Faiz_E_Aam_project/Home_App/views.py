from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *


# Create your views here.
def Home_Page(request):
    urlType = "upi://pay?pa=paytmqrhnba42ds49@paytm&cn=CAD&pn=Paytm"
    urlType1 = "upi://pay?pa=paytmqrhnba42ds49@paytm&am="
    urlType2 = "&cn=CAD&pn=Paytm"

    return render(request,'index.html')

def About_Page(r):
    return render(r,'about.html')

def Blog_Page(request):
    blog_content = Blog.objects.all()
    context = {'data':blog_content}
    return render(request,'blog.html',context)


def blog_post_detail(request, slug):
    blog_post = get_object_or_404(Blog, slug=slug)
    return render(request, 'post_detail.html', {'blogs': blog_post})





def Contact_Page(r):
    return render(r,'contact.html')

def Donate_Page(r):
    return render(r,'donate.html')

def Gallery_Page(r):
    return render(r,'gallery.html')

def Services(r):
    return render(r,'donation.html')

def Demo(r):
    data = Data.objects.all()
    return render(r,'demo.html',{'data':data})

# all ajax form submiting request startr here
@csrf_exempt
def Become_volunteer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email') 
        number = request.POST.get('number') 
        message = request.POST.get('message') 
        Volunteers.objects.create(name = name , email = email , number = number , message = message)
        return HttpResponse('<h2 class="text-light border rounded text-center fs-1 fw-bold">Submit successfully </h2>')
    else:
        return HttpResponse('error')

@csrf_exempt
def ContactUsForm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email') 
        number = request.POST.get('number') 
        message = request.POST.get('message') 
        ContactUs.objects.create(name = name , email = email , number = number , message = message)
        return HttpResponse('<h2 class="text-success border rounded text-center fs-1 fw-bold">Submit successfully </h2>')
    else:
        return HttpResponse('error')
    
