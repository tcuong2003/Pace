from django.shortcuts import render

# Create your views here.
def pace_seminar_form(request):
    return render(request, 'pace_seminar_form.html')