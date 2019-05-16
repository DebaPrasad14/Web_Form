from django.shortcuts import render,  redirect
from django.contrib import messages
from .models import UserField


def home(request):
    return render(request, 'html/home.html',{})


def webform(request):
    return render(request, 'html/form.html', {})


def webform_submit(request):
    if request.method =='POST':

        try:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            job_title = request.POST['job_title']
            resume = request.POST['document']

        except Exception as e:
            messages.success(request, e)
            return render(request, 'html/form.html', {})

        user_info = UserField(name = name, email = email, phone = phone,
                                                                job_title = job_title, resume = resume)
        user_info.save()
        messages.success(request,"Good Job !! Your Details are successfully saved in DB")
        return render(request, 'html/form.html', {})


def about(request):
    my_name = "Deba Prasad"
    company = "AMDOCS DVCI, PUNE"
    address = "PUNE"
    context = {"name":my_name, "company":company, "address":address}
    return render(request,'html/about.html', context)
