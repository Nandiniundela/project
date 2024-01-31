from django.urls import path
from apis.v1 import views

urlpatterns = [
    path("get_bus",views.all_buses),
    path("add_bus",views.add_bus),
    path("edit_bus",views.edit_bus),
    path("put_bus",views.put_bus),
    path("delete_bus",views.delete_bus),
    path("one_busdetail/<int:num>",views.one_busdetail)

    
]
