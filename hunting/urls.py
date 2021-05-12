from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<uuid:id>/', views.StageView.as_view(), name='stage'),
    path('<uuid:id>/check/', views.check_stage, name='check'),
]
