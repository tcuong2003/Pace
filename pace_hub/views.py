from django.shortcuts import render

# Create your views here.
def pace_hub_form(request):
    return render(request, 'pace_hub_form.html')