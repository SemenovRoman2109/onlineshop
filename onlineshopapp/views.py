from django.shortcuts import render

# Create your views here.
def show_main(request):
    return render(request,"main.html")
                  
def show_catalogue(request):
    return render(request,"catalogue.html")

def show_about_us(request):
    return render(request,"about_us.html")

def show_feedback(request):
    return render(request,"feedback.html")