from django.shortcuts import render

# Create your views here.
def pace_npo_form(request):
    return render(request, 'pace_npo_form.html')