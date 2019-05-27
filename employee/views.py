from django.shortcuts import render
from .models import InformationEmployee, Position

# Create your views here.
def home(request):
    employee = InformationEmployee.objects.all()
    context = {'employee':employee}
    return render(request,'basic.html', context)