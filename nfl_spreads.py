# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:44:21 2020

@author: kathy
"""

"""Part II ­ NFL  (in case you have trouble with the Apple prices)"""

import requests
import lxml.html as lh
import pandas as pd

"""SOURCE OF BELOW SOLUTION: https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059"""

URL = "http://www.footballlocks.com/nfl_point_spreads_week_4.shtml"
page = requests.get(URL) 
  
doc = lh.fromstring(page.content)

tr_elements = doc.xpath('//tr')

"""FIND ALL ROWS WITH FOUR COLUMNS"""
position = []
for T in tr_elements:
    if len(T) == 4:
        position.append(tr_elements.index(T))
    
print(f"Here are the positions where four columns appear in the table: {position} \n")

col=[]
i=0

"""PRINT HEADERS FROM ROW 50 (ROW 4 IS AN ANOMALY)"""
for t in tr_elements[50]:
    i+=1
    name=t.text_content()
#    print ('%d:"%s"'%(i,name))
    col.append((name,[]))

"""LOOPING LIST THROUGH ROW 2 THROUGH 33 (AVOIDING LAST ROW BECAUSE IT DOES NOT CONFORM TO 19 ROWS)"""    
for j in range(51,294):
    T=tr_elements[j]
     
    if len(T)!=4:
        break
    
    i=0
    
    for t in T.iterchildren():
        data=t.text_content() 
        
        col[i][1].append(data)

        i+=1
        
Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)

print(f"Here are the top five of the spread from the website: \n {df.head()} \n")

def retrieve_team_spreads(team):
    df1 = df[df['Favorite'].str.contains(team) | df['Underdog'].str.contains(team)] 
    print(f"\nHere are the games where {team} played: \n {df1}") 
    
retrieve_team_spreads('Chargers')
