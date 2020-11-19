from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def About(request):
    return render(request, "about.html")


def Sidebar_Left(request):
    return render(request, "sidebar-left.html")


def Contact(request):
    return render(request, "contact.html")


def Sidebar_Right(request):
    return render(request, "sidebar-right.html")
