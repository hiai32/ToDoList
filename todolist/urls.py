from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.home, name='home'),
    path('add/<int:user_id>/', views.add, name='add'),
    path('update/<int:user_id>/<int:task_id>/', views.update, name='update'),
    path('mypage/<int:user_id>/', views.mypage, name='mypage'),
    path('search/<int:user_id>/', views.search, name='search'),
]
