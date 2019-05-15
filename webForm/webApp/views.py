from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'html/index.html',{})


def about(request):
    my_name = "Deba Prasad"
    company = "AMDOCS DVCI, PUNE"
    address = "PUNE"
    context = {"name":my_name, "company":company, "address":address}
    return render(request,'html/about.html', context)
