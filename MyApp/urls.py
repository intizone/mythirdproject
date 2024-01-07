from django.urls import path
from .views import *

app_name = 'MyApp'

urlpatterns = [
    path("", home, name="home"),
    path("services/view/", view_services, name="view_services"),
    path("news/view/", view_news, name="view_news"),

    path("services/update/", update_service, name="update_service"),
    path("news/update/", update_news, name="update_news"),

    path("services/delete/", delete_service, name="delete_service"),
    path("news/delete/", delete_news, name="delete_news"),

    path("services/create/", create_service, name="create_service"),
    path("news/create/", create_news, name="create_news"),
]
