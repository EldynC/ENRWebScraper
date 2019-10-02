from bs4 import BeautifulSoup #Import BeautifulSoup for scraping
import urllib3 #Import urllib3 to create http requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.enr.com/texas-louisiana/toplists/2019-top-contractors' #Store website URL


def make_soup(url): #soup function start
    http = urllib3.PoolManager()
    r = http.request("GET", url) #create an HTTP request
    soup = BeautifulSoup(r.data ,'lxml')  #create a soup object
    table = soup.findAll('tbody', {'cellpadding': None}) #find all the table bodies on the website

    for row in table[0].find_all("tr")[1:110]: #loop through the entire table and find all the elements with a tr attribute
        print("\"" + row.find("strong").get_text() + "\"" + " OR") #Create a boolean string for all the names of the companies

#end of soup function
make_soup(url) #call soup function to create boolean string


