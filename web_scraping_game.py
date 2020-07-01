import requests
from bs4 import BeautifulSoup
import random

print('\n' * 10)
print('Give us a sec to scrape all the quotes for you :)')
print('\n' * 21)

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

answers = 4
wanna_play = True
while wanna_play:
    quote = random.choice(_scraped)
    author = quote['author']
    print(quote['text'])
    while answers > 0:
        answer = input('Try to guess the author of this quote : \n')
        if answer != author:
            answers -= 1
            print(f'Nooo, that\'s not right. {answers} left')
            if answers == 3:
                letter = author[0]
                print(f'Here\'s a hint! The first name of the author starts with {letter}')
            elif answers == 2:
                position = author.find(' ')
                letter = author[position+1]
                print(f'Here\'s a hint! The last name of the author starts with {letter}')
            elif answers == 0:
                print(f'You lost! The correct answer was {author}')
            
        else:
            print('Congratulations! That\'s right!')
            break
    wants_more = input('You wanna play again?')
    if wants_more.lower() in ['y', 'yes', 'yeah', 'sure']:
        answers = 4
    else:
        print('Thanks for playing!')
        wanna_play = False

