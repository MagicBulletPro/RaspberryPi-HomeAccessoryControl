from django.urls import path
from . import views


urlpatterns = [
    path('', views.accessory_list, name='accessory_list'),
    path('toggle/<int:accessory_id>/', views.toggle_accessory, name='toggle_accessory'),
]