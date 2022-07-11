import requests
import re
from bs4 import BeautifulSoup



#base URL from which the rhyming function will construct a url to scrape from


BASE_URL= "https://rhymer.com/"


def scrape_page(word):

    """When a user imputs a word in rhymer.com, they are redirected to a page
    which displays all the words that rhhyme with the word the user imputted. This function
    scrapes the content of that page."""


    html_text = requests.get(BASE_URL + f"{word}.html").text
    soup = BeautifulSoup(html_text, "html.parser")
    words = soup.find_all("a", class_= "btn c")

  #  return words[0].text


    rhyming_words = []

    for i in range(len(words) - 1):
        rhyme = words[i]
        rhyme = rhyme.text
        #last_chars = word[-2:]

        #rhyme = re.split(last_chars, rhyme)
        #rhyme = rhyme + last_chars
        rhyming_words.append(rhyme)
    return rhyming_words




def find_rhyme(word):

    """This is a function that uses the data scraped from the scraper function
    and presents it into a nice list of words that rhyme """#

    if type(word) != "<class 'str'>":
        raise ValueError("Non string types are not allowed here")

    pass

#print(scrape_page("horse"))


char = "horse"
print(scrape_page("horse"))
