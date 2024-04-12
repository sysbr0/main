from django.urls import path
from  . import views

urlpatterns = [

    path('main',views.index, name='index'),
      path('about',views.about, name='about'),
          path('navbar',views.navbar, name='navbar'),
    path('index2',views.index2, name='ibdex2'),
        path('navbar2',views.navbar2, name='navbar2'),
         path('indix',views.indix, name='indix'),
    path('books',views.book_list, name='book'),
       path('fatch',views.fatch, name='fatch'),
       path('filter',views.filter, name='filter'),

    path('bookk/<str:isbn>/', views.book_detail, name='book_detail'),
       path('ty',views.bookdt, name='ty'),
  path('booko/<str:isbn>/', views.bk, name='bk'),

      path('book/<int:cid>/<str:iso>/', views.bk_detail, name='bk_detail'),
]

