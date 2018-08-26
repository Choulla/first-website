from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:id_blog>/',views.detail, name="detail"),
]