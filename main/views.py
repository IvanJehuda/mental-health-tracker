from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152222',
        'name': 'Ivan Jehuda Angi',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)