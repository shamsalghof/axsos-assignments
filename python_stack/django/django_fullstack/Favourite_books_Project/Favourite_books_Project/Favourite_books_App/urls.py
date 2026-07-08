from django.urls import path
from . import views

urlpatterns = [
    #Authentication
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('check_email/', views.check_email_ajax, name='check_email'),

    path('create_book', views.create_book, name='create_book'),
    path('book/<int:book_id>', views.book_info,name='book_info'),
    path('book/update_book/<int:book_id>',views.update_book,name='update_book'),

    path('books/<int:book_id>/delete', views.delete_book, name='delete_book'),
    path('books/<int:book_id>/favorite', views.favorite_book, name='favorite_book'),
    path('books/<int:book_id>/unfavorite', views.unfavorite_book, name='unfavorite_book'),
]