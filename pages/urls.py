from django.urls import path
from  . import views

urlpatterns = [

    path('main',views.index, name='index'),
      path('about',views.about, name='about'),
          path('navbar',views.navbar, name='navbar'),
    path('index2',views.index2, name='ibdex2'),
        path('navbar2',views.navbar2, name='navbar2'),
         path('indix',views.indix, name='indix'),
    path('book',views.book_list, name='book'),
       path('fatch',views.fatch, name='fatch'),
 
]

