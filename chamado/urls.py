from django.urls import path
from .views import MudarEstadoChamadoView, HomeChamadoView, CreateChamadoView, ReadChamadoView, EditChamadoView, DeleteChamadoView, ReadClosedChamadoView, ReadOpenChamadoView, OwnerChamadoView


app_name = 'chamado'
urlpatterns = [
    path('home/', HomeChamadoView.as_view(), name='home'),
    path('create/', CreateChamadoView.as_view(), name='create'),
    path('read/', ReadChamadoView.as_view(), name='read'),
    path('edit/<int:pk>/', EditChamadoView.as_view(), name='edit'),
	path('delete/<int:pk>/', DeleteChamadoView.as_view(), name='delete'),
	#path('close/<int:pk>/', CloseChamadoView.as_view(), name='close'),
	#path('open-again/<int:pk>/', OpenAgainChamadoView.as_view(), name='open-again'),
	path('owner/<int:pk>/', OwnerChamadoView.as_view(), name='owner'),
	path('read-closed/', ReadClosedChamadoView.as_view(), name='read-closed'),
	path('read-open/', ReadOpenChamadoView.as_view(), name='read-open'),
	path('change-status/<int:pk>/', MudarEstadoChamadoView.as_view(), name='change-status'),
]
