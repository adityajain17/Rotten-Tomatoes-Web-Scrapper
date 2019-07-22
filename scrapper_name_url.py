from selenium import webdriver
import bs4
import requests
import urllib
from bs4 import BeautifulSoup as bsp

driver=webdriver.Chrome('e:/chromedriver')
toscrape=[
    'https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_art_house__international_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_classics_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_comedy_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_documentary_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_drama_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_horror_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_kids__family_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_musical__performing_arts_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_mystery__suspense_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_romance_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_science_fiction__fantasy_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_special_interest_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_sports__fitness_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_television_movies/',
    'https://www.rottentomatoes.com/top/bestofrt/top_100_western_movies/'
]

genres=['Action|Adventure','Animation','Art house','Classic','Comedy','Documentary','Drama','Horror','Kids|Family','Musical','Mystery','Romance','Science Fiction','Special interest','Sports fitness','Telivision','Western']

urls=[]
for  x in toscrape:
    driver.get(x)
    html=driver.page_source
    soup = bsp(html)
    genre=[]
    for a in soup.find('table',class_='table').findAll('a',class_='unstyled articleLink'):
        genre.append(a['href'])
    urls.append(genre)

driver.close()
with open('url2.txt','w') as f:
    m=0
    g=0
    f.write('url,genre\n')
    for i in urls:
        for j in i:
            f.write('https://www.rottentomatoes.com'+j+','+genres[g]+'\n')
            m+=1
        g+=1
