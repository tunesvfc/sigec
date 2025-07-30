from django.urls import path

from .views import IndexCoreView

app_name = 'core'

urlpatterns = [
    path('', IndexCoreView.as_view(), name='index'),
]
