from django.urls import path
from .views import *


urlpatterns =[
    path("get_category_name/", get_category_name),
    path("get_home_at_your_department/", get_home_at_your_department),
    path("get_home_connection1/", get_home_connection1),
    path("get_home_connection2/", get_home_connection2),
    path("get_all_products/", get_all_products),
    path("category/<int:pk>/", get_size),
    path("get_color/<int:pk>/", get_color),
    path("get_name/<int:pk>/", get_name),
]