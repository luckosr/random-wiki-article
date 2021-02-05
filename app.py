import wikipedia as wiki
from string import Template
import datetime


def randomArticle():
    random = wiki.random()

    string = Template(
        'Do you want to read this article: "$random" ?').substitute(random=random)
    print(string)
    return random


def saveRead(article):
    date = datetime.datetime.now()
    file = open('./readArticles.txt', 'a', encoding='utf-8')
    file.write(Template('"$article" read $date').substitute(
        article=article, date=date))
    file.close()


def start():

    random = randomArticle()
    answer = input('Please enter Yes or No \n')
    if answer == 'Yes':
        print(wiki.page(random).content)
        saveRead(random)
    elif answer == 'No':
        start()


start()
