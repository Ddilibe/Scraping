#Django Import 
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import NewsArticle

# Module Import 
import requests
from bs4 import BeautifulSoup


"""
    Section for the views contained in python
"""
class NewsListView(ListView):
    model = NewsArticle
    template_name = "list.html"
    
        
class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = "detail.html"
    

"""
    Section for the scraping Process
    
"""
# Scrapes the website and store all potential links that has news articles within in a file called jaden

    
    
def Script_and_Store_in_a_file():
    jaden = open('jaden.txt','w')
    response = requests.get("https://www.naijanews.com/")
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('section', {'class':'mvp-widget-home'})
    for i in links:
        i = i.find('a')
        i = i['href']
        jaden.writelines(i)
        jaden.writelines('\n')
    jaden.close()

#Opens a file called Jaden
def open_file():
    file = open('jaden.txt', 'r')
    return file


#Listing all the websites in jaden, it scrapes it and stores it in the sqlite database
def Scraping_multiple_websites(file): 
    NewsArticle.objects.all().delete()
    num = 1
    for i in file:
        p = " "
        response = requests.get(i)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', {'class':'mvp-post-title left entry-title'})
        title = title.string
        if title not in ["None"] :
            title = title
        else:
            title = "This title has no flaw amazing"
        slug_title = title.split()
        slug_title = "".join(slug_title)
        print(title)
        image = soup.find('div', {'id':'mvp-post-content'})
        image = image.find('img')
        if image != 'None':
            image = image['src']
        else:
            image = ('www.google.com')
        texts = soup.find('div', {'id':'mvp-content-main'})
        texts = texts.find_all('p')

        for i in texts:
            i = i.get_text()
            if i not in p:
                p = p + str(i)
            else: 
                continue
        NewsArticle.objects.create(
            id = num,
            title = title,
            slug = slug_title,
            image_url = image,
            body = p,
        ).save()
    
        num += 1
        if num >= 10:
                break

#Closes the file, typically the jaden file
def close_file(file):
    file.close()

"""
    Runs each function individually
"""

Script_and_Store_in_a_file()
file = open_file()
Scraping_multiple_websites(file)
close_file(file)