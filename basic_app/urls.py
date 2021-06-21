from django.urls import path
from basic_app.views import other, relative_url

app_name = 'basic_app'

urlpatterns = [

    path('other/', other, name='other'),
    path('relative/', relative_url, name='relative_url')
]
