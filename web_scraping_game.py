import requests
from bs4 import BeautifulSoup
import random

print('\n\n\n\n\n\n')
print('Give us a sec to scrape all the quotes for you :)')

_scraped = []
next_page = "/"

while next_page:
    html = requests.get(f'http://quotes.toscrape.com' + next_page)
    response = BeautifulSoup(html.text, "html.parser")
    quotes = response.find_all("div", ["quote"])
    buttons = response.find_all("li", ["next"])

    for quote in quotes:
        text = quote.find("span").get_text()
        author = quote.find("small").get_text()
        link = quote.find("a")['href']
        _scraped.append({"author": author, "link": link, "text": text})
    
    if buttons:
        for button in buttons:
            next_page = button.find("a")['href']
    else:
        next_page = False

answers = 5
wanna_play = True
while wanna_play:
    quote = random.choice(_scraped)
    author = quote['author']
    print('\n\n\'')
    print(quote['text'])
    print('\n\n\'')
    while answers > 0:
        answer = input('Try to guess the author of this quote : \n')
        if answer != author:
            answers -= 1
            print(f'Nooo, that\'s not right. {answers} left')
            if answers == 4:
                letter = author[0]
                print(f'Here\'s a hint! The first name of the author starts with {letter}')
            if answers == 3:
                position = author.find(' ')
                letter = quote['author'][position+1]
                print(f'Here\'s a hint! The last name of the author starts with {letter}')
            if answers == 0:
                print(f'You lost! The correct answer was {author}')
            
        else:
            print('Congratulations! That\'s right!')
            break
    wants_more = input('You wanna play again?')
    print('\n')
    if wants_more.lower() in ['y', 'yes', 'yeah', 'sure']:
        answers = 5
    else:
        print('Thanks for playing!')
        wanna_play = False

