
import requests
from bs4 import BeautifulSoup
import re



#base URL from which the rhyming function will construct a url to scrape from


BASE_URL= "https://rhymer.com/"



def scrape_page(word, j=20):

    """When a user imputs a word in rhymer.com, they are redirected to a page
    which displays all the words that rhyme with the word the user imputted. This function
    scrapes all the rhymes present in that page and returns a list of unclean data"""


    html_text = requests.get(BASE_URL + f"{word}.html").text
    soup = BeautifulSoup(html_text, "html.parser")

    unclean_data = []
    for i in range (1,j+1):

        word = soup.find_all("div", id= f"syl-{i}")
        if len(word) != 0:
            unclean_data.append(word)

    return unclean_data



def clean_data(unclean_data):

    """This function takes the unclean list of data returned by the scrape_data
    function and cleans it, putting the words into a lis."""

    rhyming_words = []
    for i in range(0, len(unclean_data) -1):

        word = str(unclean_data[i])
        newstring = re.sub(r"[^a-zA-Z]+", "", word)
        newstring = newstring.split("html")

        for string in newstring[:-1]:
            string = string.split("href")

            newstring[-1].rstrip("div")
            rhyming_words.append(string[1])
    return rhyming_words




def find_rhyme(word, syllables=None):


    """This is a function that uses the data scraped from the scraper function
    and presents it into a nice list of words that rhyme. It takes two parameters, the word
    the user would like to find rhyming words for and an optional parameter,
    the syllable parameter. There the user can input an integer that specifies how many
    syllables they woud like the rhyming word to have. If not specified the function
    will return a list of all the words that rhyme with it """


    if  isinstance(word, str):
        if syllables == None:
            unclean_data = scrape_page(word)
            return clean_data(unclean_data)

        if  not isinstance(syllables, int):
            raise ValueError("Non integer types are not allowed here")

        if  syllables < 1:
            raise ValueError("Integer for syllables must be positive")

        if syllables >= 1:
            rhymes=[]
            unclean_data= scrape_page(word, syllables)[-1]
            word = str(unclean_data)
            newstring = re.sub(r"[^a-zA-Z]+", "", word)
            newstring = newstring.split("html")
            for string in newstring[:-1]:
                string = string.rstrip("div")
                string = string.split("href")

                rhymes.append(string[1])
            return rhymes

    else:
        raise ValueError("Non string types are not allowed here")
