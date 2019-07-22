import pandas as pd
from bs4 import BeautifulSoup as bsp
from selenium import webdriver
 
df=pd.read_csv('url2.txt')
genres=['Action|Adventure','Animation','Art house','Classic','Comedy','Documentary','Drama','Horror','Kids|Family','Musical','Mystery','Romance','Science Fiction','Special interest','Sports fitness','Telivision','Western']
toscrape=list(df.url[df.genre==genres[16]])
driver=webdriver.Chrome('e:/chromedriver')
# for i in toscrape:
# temp=toscrape[0]
data={
      'title':[],
    'synopsis':[],
    'genre':[],
    'director':[],
    'writers':[],
    'intheatre':[],
    'streaming':[],
    'image':[],
    'tomatometer':[],
    'audiencescore':[]
}
cnt=0
m=[]
for temp in toscrape:
    try:
        driver.get(temp)
        soup=bsp(driver.page_source)
        title=soup.find('h1',{'class':'mop-ratings-wrap__title mop-ratings-wrap__title--top'}).getText()
        synopsis=soup.find('div',{'id':'movieSynopsis'}).getText()
        info=soup.findAll('div',class_='meta-value')
        genre='|'.join([i.getText() for i in info[1].findAll('a')])
        director='|'.join([i.getText() for i in info[2].findAll('a')])
        writers='|'.join([i.getText() for i in info[3].findAll('a')])
        intheatre=info[4].find('time').getText()
        streaming=info[5].find('time').getText()
    #    runtime=info[7].find('time').getText()
    #    studio='|'.join([i.getText() for i in info[8].findAll('a')])
        image_url=soup.find('a',{'id':'poster_link'}).find('img')['data-src'] if soup.find('a',{'id':'poster_link'}) else soup.find('div',{'id':'topSection'}).find('img')['data-src']
        tomatometer=soup.find('span',{'class':'mop-ratings-wrap__percentage'}).getText()
        audiencescore=soup.findAll('span',{'class':'mop-ratings-wrap__percentage'})[1].getText()
        data['synopsis'].append(synopsis)
        data['title'].append(title)
        data['genre'].append(genre)
        data['director'].append(director)
        data['writers'].append(writers)
        data['intheatre'].append(intheatre)
        data['streaming'].append(streaming)
    #    data['runtime'].append(runtime)
    #    data['studio'].append(studio)
        data['image'].append(image_url)
        data['tomatometer'].append(tomatometer)
        data['audiencescore'].append(audiencescore)
    except:
        m.append(title)
    if cnt%10==0:
        print(cnt)
    cnt+=1
df2=pd.DataFrame(data)
df2.to_csv('animation.csv')
