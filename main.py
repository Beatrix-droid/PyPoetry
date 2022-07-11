
import requests
from bs4 import BeautifulSoup



#base URL from which the rhyming function will construct a url to scrape from


BASE_URL= "https://rhymer.com/"


def scrape_page(word):

    """When a user imputs a word in rhymer.com, they are redirected to a page
    which displays all the words that rhyme with the word the user imputted. This function
    scrapes all the rhymes present in that page."""


    html_text = requests.get(BASE_URL + f"{word}.html").text
    soup = BeautifulSoup(html_text, "html.parser")
    words = soup.find_all("a", class_= "btn c")

    rhyming_words = []

    for i in range(len(words) - 1):
        rhyme = words[i]
        rhyme = rhyme.text

        rhyming_words.append(rhyme)
    return rhyming_words




def find_rhyme(word, syllables=None):

    """This is a function that uses the data scraped from the scraper function
    and presents it into a nice list of words that rhyme. It takes two parameters, the word
    the user would like to find rhyming words for and an optional parameter,
    the syllable parameter. There the user can input an integer that specifies how many
    syllables they woud like the rhyming word to have. If not specified the function
    will return a list of all the words that rhyme witht eh """


    if  isinstance(word, str):
        if not syllables:
            return scrape_page(word)
        else:
            pass
    else:
        raise ValueError("Non string types are not allowed here")





#print(scrape_page("horse"))


#print(type("horse"))
