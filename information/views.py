from django.shortcuts import render

# Create your views here.
from .models import Information
def info(request):
    information = Information.objects.all()
    return render(request, 'information/index.html', {'information': information})

def patient(request, patient_id):
    info = Information.objects.get(id=patient_id)
    return render(request, 'information/patient.html', {'info': info ,"doctors": info.doctors.all()})