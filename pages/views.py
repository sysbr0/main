from django.shortcuts import render
from .neo4j_service import Neo4jService
from .neo4j_http_service import Neo4jHTTPService



# Create your views here.

def index(request) :
  
  return  render(request, 'pages/sydnavi.html' , { 'name' : 'ahmed'})


def about(request) :
     return  render(request, 'pages/index.html' , { 'name' : 'ahmed'})

from django.shortcuts import render

def navbar(request):
    social_media_links = [
        {
            'platform': 'instagram',
            'url': 'https://www.instagram.com/your_instagram_username',
            'icon_class': 'fab fa-instagram fa-lg',
        },
        {
            'platform': 'youtube',
            'url': 'https://www.youtube.com/your_youtube_channel',
            'icon_class': 'fab fa-youtube fa-lg',
        },
        {
            'platform': 'facebook',
            'url': 'https://www.facebook.com/your_facebook_page',
            'icon_class': 'fab fa-facebook fa-lg',
        },
        {
            'platform': 'email',
            'url': 'mailto:your_email@example.com',
            'icon_class': 'fa-solid fa-envelope',
        },
        {
            'platform': 'whatsapp',
            'url': 'https://wa.me/your_whatsapp_number',
            'icon_class': 'fab fa-whatsapp fa-lg',
        },
    
      
    ]
    menu =[ 
        {
          'name': 'facebook',
            'link': 'https://www.facebook.com/your_facebook_page'
        },

          {
          'name': 'facebook',
            'link': 'https://www.facebook.com/your_facebook_page'
        },
          {
          'name': 'facebook',
            'link': 'https://www.facebook.com/your_facebook_page'
        },
          {
          'name': 'facebook',
            'link': 'https://www.facebook.com/your_facebook_page'
        },
          {
          'name': 'facebook',
            'link': 'https://www.facebook.com/your_facebook_page'
        },
          {
          'name': 'facebook',
            'link': 'https://www.facebook.com/your_facebook_page'
        },
     ]


    return render(request, 'base/navbar.html', {'social_media_links': social_media_links, 'menu': menu})


def index2(request) :
     books = [
        {
            'ISBN': '195153448',
            'title': 'Classical Mythology',
            'author': 'Mark P. O. Morford',
            'year_of_publication': '2002',
            'publisher': 'Oxford University Press',
            'image_url': 'http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg'
        },
        {
            'ISBN': '2005018',
            'title': 'Clara Callan',
            'author': 'Richard Bruce Wright',
            'year_of_publication': '2001',
            'publisher': 'HarperFlamingo Canada',
            'image_url': 'http://images.amazon.com/images/P/0002005018.01.LZZZZZZZ.jpg'
        },
        # Add more books similarly
             ]
     return  render(request, 'pages/index2.html' ,{'books': books})  

def navbar2(request) :
     
     
     return  render(request, 'base/navbar2.html' )

def indix(request) :
      books = [
        {
            'ISBN': '195153448',
            'title': 'Classical Mythology',
            'author': 'Mark P. O. Morford',
            'year_of_publication': '2002',
            'publisher': 'Oxford University Press',
            'image_url': 'http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg'
        },
        {
            'ISBN': '2005018',
            'title': 'Clara Callan',
            'author': 'Richard Bruce Wright',
            'year_of_publication': '2001',
            'publisher': 'HarperFlamingo Canada',
            'image_url': 'http://images.amazon.com/images/P/0002005018.01.LZZZZZZZ.jpg'
        },
        # Add more books similarly
             ]
     
      return  render(request, 'pages/index.html',{'books': books} )




def my_view(request):
    neo4j_http_service = Neo4jHTTPService(NEO4J_HTTP_URI, NEO4J_USERNAME, NEO4J_PASSWORD)
    result = neo4j_http_service.run_query("MATCH (n) RETURN n LIMIT 5")
    nodes = result['results'][0]['data']
    
    return render(request, 'pages/template.html', {'nodes': nodes})
