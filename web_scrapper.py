from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanicalsoup as ms
from nltk.corpus import words
import random
import csv

browser=ms.StatefulBrowser(user_agent="MechanicalSoup")
urls=[]

for j in ['train','valid']:
  no=[300 if j=='train' else 50]
  count=0
  print(no)
  while count<no[0]:

    n=random.randint(0,236736)
    word=words.words()[n]


    browser.open("https://duckduckgo.com/")
    browser.select_form('#search_form_homepage')
    browser['q']=word
    browser.submit_selected()


    for n,i in enumerate(browser.page.select('a.result__a')):
  
      content=[]
      url=i.attrs['href']
      if url in urls:continue
      urls.append(url)

      
      lis=url.split(".")
      try:
          index=lis.index("https://www") + 1
      except:
          continue

      try:
          page = urlopen(url,timeout=10).read().decode(encoding="iso-8859-1")
      except:
          continue

      soup = BeautifulSoup(page, 'html.parser')
      remove=[]

      for link in soup("link"):link.decompose()
      for meta in soup("meta"):meta.decompose()
      for head in soup("head"):head.decompose()
      for script in soup("script"):soup.script.extract()
      for style in soup("style"):style.decompose()
      for img in soup("img"):img.decompose()
      REMOVE_ATTRIBUTES = ['lang','language','onmouseover','onclick','id','onload','onmouseout','script',
                          'dir','face','class','hspace','text']


      for attr_del in REMOVE_ATTRIBUTES: 
          [s.attrs.pop(attr_del) for s in soup.find_all() if attr_del in s.attrs]

      text=str(soup)+'\n\n<|endoftext|>\n\n'
      
        
      
      
      with open(f'{j}.txt', 'a') as f:
         f.write(text)
         f.close()
      print(count)
      count+=1
    
  
