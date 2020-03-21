# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 11:03:52 2020

@author: kathy
"""

"""Part I ­ CBS Football Stats"""

import requests
import lxml.html as lh
import pandas as pd

"""SOURCE OF BELOW SOLUTION: https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059"""

URL = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns"
page = requests.get(URL) 
  
doc = lh.fromstring(page.content)

tr_elements = doc.xpath('//tr')

"""PRINT FIRST 10 ROWS TO SEE STANDARD COLUMN LENGTH"""
print(f"Here are the top 10 rows of the table: \n {[len(T) for T in tr_elements[0:10]]}\n")

"""PRINT LENGTH OF LIST"""
print(f"This is the length of the entire table: {len(tr_elements)}\n")

"""PRINT LAST FIVE ROWS TO SEE WHERE TO STOP THE LIST NOT CONFORMING TO 19 COLUMNS"""
print(f"Here are the last five rows of the table: {[len(T) for T in tr_elements[30:34]]}\n")

col=[]
i=0

"""PRINT COLUMN HEADERS FROM ROW 2 - WHERE TABLE BEGINS"""
for t in tr_elements[2]:
    i+=1
    name=t.text_content()
#    print ('%d:"%s"'%(i,name))
    col.append((name,[]))


"""LOOPING LIST THROUGH ROW 2 THROUGH 33 (AVOIDING LAST ROW BECAUSE IT DOES NOT CONFORM TO 19 ROWS)"""    
for j in range(3,len(tr_elements) - 1):
    T=tr_elements[j]
     
    if len(T)!=19:
        break
    
    i=0
    
    for t in T.iterchildren():
        data=t.text_content() 
        
        col[i][1].append(data)

        i+=1
        
        
Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)

top20 = df.head(20)

requested_list = top20[['Player', 'Pos', 'Team', 'TD']]

print(f"Here's the top 20 players on the regular list: \n{requested_list}")