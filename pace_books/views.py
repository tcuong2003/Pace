from django.shortcuts import render

# Create your views here.
def pace_books_form(request):
    return render(request, 'pace_books_form.html')