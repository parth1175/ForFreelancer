from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_data/<data_id>', views.update_data, name='update-data'),
]
