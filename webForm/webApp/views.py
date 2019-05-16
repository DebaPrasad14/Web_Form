from django.shortcuts import render,  redirect

# Create your views here.

def home(request):
    return render(request, 'html/home.html',{})


def webform(request):
    return render(request, 'html/form.html', {})

def getDetails(request):
    pass


def about(request):
    my_name = "Deba Prasad"
    company = "AMDOCS DVCI, PUNE"
    address = "PUNE"
    context = {"name":my_name, "company":company, "address":address}
    return render(request,'html/about.html', context)
