from django.urls import path
from .views import create_view_vehicle, delete_view, detail_view, create_view, detail_view_vehicle, list_view, list_view_log, list_view_vehicle, update_view, view_log, view_vehicle

urlpatterns = [
    path('', list_view ,name ="list"),
    path('create', create_view, name='create'),
    path('<int:id>', detail_view, name='detail'),
    path('<int:id>/update', update_view, name='update'),
    path('<int:id>/delete', delete_view, name='delete'),
    path('<int:id>/viewvehicle', view_vehicle, name='view_vehicle'),

    path('vehicle', list_view_vehicle, name='list_vehicle'),
    path('vehicle/create', create_view_vehicle, name='create_vehicle'),
    path('vehicle/<int:id>', detail_view_vehicle, name='detail_vehicle'),
    # path('vehicle/<int:id>/update', update_view, name='update'),
    path('<int:id>/viewlog', view_log , name='view_log'),

    path('parkinglog', list_view_log, name='list_log'),
    
]