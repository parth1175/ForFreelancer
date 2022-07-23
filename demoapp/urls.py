from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_data/<int:data_id>', views.update_data, name='update-data'),
    path('update_data/updaterecord/<int:data_id>', views.updaterecord, name='updaterecord'),
    path('delete/<int:id>', views.delete, name='delete'),

]
