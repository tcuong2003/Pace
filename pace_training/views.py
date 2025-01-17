from django.shortcuts import render

# Create your views here.
def pace_training_form(request):
    return render(request, 'pace_training_form.html')