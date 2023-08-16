from django.urls import path
from . import views

urlpatterns = [
	path('',views.show),
	path('posts',views.posts,name="posts"),
	path('get-one/<str:pk>/',views.getOne,name='get-one'),
	path('delete/<str:pk>/',views.delete,name='delete'),
	path('get-update/<str:pk>/',views.getUpdate,name='get-update')

]