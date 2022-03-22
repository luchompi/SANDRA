from django.urls import path 
from . import views as v
app_name="colegio"


urlpatterns =[
path('sedes/',v.SedeListView.as_view(),name="sedeIndex"),
path('sedes/nuevo',v.SedeCreateView.as_view(),name="sedeCreate"),

]