from django.shortcuts import render, HttpResponse

# Create your views here.


def login(request):
    # return HttpResponse("Hello,django")
    return render(request, "login.html", )
