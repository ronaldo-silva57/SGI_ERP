from django.shortcuts import render

def help_home(request):
    return render(request, 'help_sgi/help_home.html')