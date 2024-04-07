from django.urls import path
from  . import views

urlpatterns = [

    path('main',views.index, name='index'),
      path('about',views.about, name='about'),
          path('navbar',views.navbar, name='navbar'),
    path('index2',views.index2, name='ibdex2'),
        path('navbar2',views.navbar2, name='navbar2'),
         path('indix',views.indix, name='indix'),
               path('neo4j',views.my_view, name='neo4j'),
]

