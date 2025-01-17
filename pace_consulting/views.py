from django.shortcuts import render

# Create your views here.
def pace_consulting_form(request):
    return render(request, 'pace_consulting_form.html')