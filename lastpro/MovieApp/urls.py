from django.urls import path
from MovieApp import views
app_name='Movie_App'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('categories/',views.category_detail,name='category_list'),
    path('category/<int:category_id>/',views.detail_category,name='detail_category')
]