from django.urls import path
from myapp2 import views
app_name="myapp2"

urlpatterns = [
    path('',views.base,name="base"),
    path('home/',views.home,name="home"),
    path('child/',views.child,name="child"),

]
