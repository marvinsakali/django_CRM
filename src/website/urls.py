from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('logout/', views.logout_user, name='logout'),
	path('register/', views.register_user, name='register'),
	path('record/', views.home, name='record'),
	path('record/<int:pk>/', views.record_detail, name='record_detail'),
	path('record/<int:pk>/delete', views.delete_record, name='delete_record'),
	path('add_record/', views.add_records, name='add_record'),
	path('update_record/<int:pk>/', views.update_record, name='update_record'),
]