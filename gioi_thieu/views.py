from django.shortcuts import render

# Create your views here.
def gioi_thieu_form(request):
    return render(request, 'gioi_thieu_form.html')