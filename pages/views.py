from django.shortcuts import render
from neo4j import GraphDatabase

from .models import Book

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



def book_list(request):
  


    # Connect to Neo4j
    neo4j_uri = "bolt://localhost:7687"
    neo4j_username = "neo4j"
    neo4j_password = "12345678"
    driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_username, neo4j_password))
   
    cypher_query = (
    "MATCH (b:Book) RETURN b LIMIT 25")

     
    with driver.session() as session:
        result = session.run(cypher_query)
        books = []
        for record in result:
            book_data = record['b']
            book = Book(
                element_id=book_data['<elementId>'],
                neo4j_id=book_data['<id>'],
                avg_age=book_data['AvgOfAge'],
                avg_book_rating=book_data['AvgOfbookRating'],
                author=book_data['Book-Author'],
                title=book_data['Book-Title'],
                isbn=book_data['ISBN'],
                image_url=book_data['Image-URL-L'],
                publisher=book_data['Publisher'],
                year_of_publication=book_data['Year-Of-Publication'],
                category_id=book_data['catagoryid'],
                category=book_data['category'],
                description=book_data['description']
            )
            books.append(book)
    
    return render(request, 'pages/template.html', {'books': books})

    


def filter(request):
   


    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345678"))
    with driver.session() as session:
        result = session.run("""
        MATCH (b:Book)
        RETURN b """)
        books = [record['b'] for record in result]




    return render(request, 'pages/template.html', {'books': books})


def fatch(request):
    
    neo4j_uri = "bolt://localhost:7687"
    neo4j_username = "neo4j"
    neo4j_password = "12345678"
    driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_username, neo4j_password))
    
    cypher_query = (

        "MATCH (c:Category {categoryId: 61})<-[:BELONGS_TO]-(book:Book) "
        "RETURN book, c"
    )
    
    books = []
    
    with driver.session() as session:
        result = session.run(cypher_query)
        for record in result:
            book_data = record['book']
            category_data = record['c']
            book = Book(
                element_id=book_data['<elementId>'],
                neo4j_id=book_data['<id>'],
                avg_age=book_data['AvgOfAge'],
                avg_book_rating=book_data['AvgOfbookRating'],
                author=book_data['Book-Author'],
                title=book_data['Book-Title'],
                isbn=book_data['ISBN'],
                image_url=book_data['Image-URL-L'],
                publisher=book_data['Publisher'],
                year_of_publication=book_data['Year-Of-Publication'],
                category_id=book_data['catagoryid'],
                category=book_data['category'],
                description=book_data['description']
            )
            books.append(book)
    
    return render(request, "pages/template.html", {'books': books})