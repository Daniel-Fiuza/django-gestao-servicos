from django.urls import path, re_path
from apps.clients.views import index


app_name= 'apps_clients'
urlpatterns = [

    # The home page
    path('clients/', index, name="clients")
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]