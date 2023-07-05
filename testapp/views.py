from django.shortcuts import render
#from testapp.forms import loginform
from testapp.models import *

def index_view(request):
    return render(request,'index.html')


def checkout_view(request):
    return render(request,'checkout.html')


def form_view(request):
    if request.method=="POST":
        if  request.POST.get('name') and request.FILES['pic'] and request.POST.get('user_name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('password'):
            model_form=seller_model()
            model_form.name=request.POST.get('name')
            model_form.user_name=request.POST.get('user_name')
            model_form.email=request.POST.get('email')
            model_form.phone=request.POST.get('phone')
            model_form.password=request.POST.get('password')
            image_file=request.FILES['pic']
            with open('media/media' + image_file.name, 'wb+') as destination:
                for chunk in image_file.chunks():
                        destination.write(chunk)
            #if request.method == 'POST':
            #image_file = request.FILES['pic']
            # Handle the uploaded file as per your requirements
            # For example, save the file to a specific folder
            #with open('media' + image_file.name, 'wb+') as destination:
             #   for chunk in image_file.chunks():
              #          destination.write(chunk)
            #model_form=seller_model(request.POST, request.FILES)
            model_form.save()
            #form_view=Login_model.objects.create(name=name,user_name=user_name,email=email,phone=phone,image=image,password=password)
            return render(request,'index.html')
    #form=loginform()
    return render(request,'form.html')

def category_view(request):

    return render(request,'category.html')

def contact_view(request):
    if request.method=="POST":
        if request.POST.get('message') and request.POST.get('name') and request.POST.get('email'):
            model_form=getouch_model()
            model_form.message=request.POST.get('message')
            model_form.name=request.POST.get('name')
            model_form.email=request.POST.get('email')
            model_form.phone=request.POST.get('phone')
            model_form.save()
            #form_view=getouch.objects.create(message=message,name=name,email=email,)
            return render(request,'index.html')
    return render(request,'contact.html')


def cart_view(request):
    return render(request,'cart.html')

def singleproduct_view(request):
    return render(request,'single-product.html')
    