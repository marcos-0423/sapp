from django.urls import path
from.import views
urlpatterns=[
path("",views.info,name="information"),
path("<int:patient_id>/",views.patient,name="patient"),
]