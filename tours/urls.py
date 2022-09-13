from django.urls import path

from . import views

urlpatterns = [
    path('', views.tours_list, name='tours_list'),
    path('tour/<int:pk>', views.tour_detail, name='tour_detail'),
    path('test', views.test_view, name='test_view'),
    path('tour/<int:pk>/generate/', views.tour_generated, name='tour_generated')
]
