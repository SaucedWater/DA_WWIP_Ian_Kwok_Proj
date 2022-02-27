##########################################
#TITLE: Python Project
#Class: PN2104L
#Name: Ian Kwok
#############

#Importing the unittest, Beautifulsoup library, urllib, urllib.request and request and the necessary files
import unittest
import requests
from bs4 import BeautifulSoup
import urllib
import urllib.request

#Class Branch - Unit testing
class MyTestMyProgram(unittest.TestCase):


    #Testing for the content in web page
    def test_contentisthere(self):
        #Set target URL
        weburl = "http://192.168.137.160/spicyx/"
        r = requests.get(weburl)
        html = r.content
        page_content = BeautifulSoup(html, "html.parser")
        content = page_content('div',{'id':'mw-content-text'})
        self.assertIsNotNone(content)
        #Display message
        print("\nContent is there")

     #testing for OK! response from website
    def test_response(self):
        #open up the connection and detect webpage response status
        response = requests.get('http://192.168.137.160/spicyx/')
        if int(response.status_code) == 200: #200 meaning website is OK!
            #Display success message
            print("\n Web scraping started at " + str('http://192.168.137.160/spicyx/'))
            print("Successful!")
            #Error checking
        else:
            print("Bad Response!")
        response.close()

    #Testing the URl and try to display all of the menus on the website
    def test_menu(self):
        with urllib.request.urlopen("http://192.168.137.160/spicyx/") as response:
            html = response.read()
            soup = BeautifulSoup(html, "html.parser")
            #Check URL for the menus
            testsite = soup.find_all('div', class_='media-body')
            for menu in testsite:
                menu_titles = menu.h4.text
                menu_price = menu.span.text
                menu_description = menu.p.text
                #display the menu
                print(menu_titles)
                print(menu_price)
                print(menu_description)


if __name__ == "__main__":
    unittest.main()
