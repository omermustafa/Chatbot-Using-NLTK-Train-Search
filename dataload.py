#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Updated on Mon May 13th 2019

@author:    Omer Mustafa
@Credits:   robinreni
"""

import pandas as pd

blogdata= pd.read_csv("techcrunch.csv")
global column
column=[]
column=blogdata.columns.tolist()

global wholelist
wholelist={}
for i in column:
    wholelist[i]=blogdata[i].values.tolist()
global catt
catt=[]

global content
content=[]

# Adding new line - start
# # Load the Pandas libraries with alias 'pd' 
# import pandas as pd 
# # Read data from file 'filename.csv' 
# # (in the same directory that your python process is based)
# # Control delimiters, rows, column names with read_csv (see later) 
# data = pd.read_csv("techcrunch.csv") 
# # Preview the first 5 lines of the loaded data 
# data.head()
# Adding new line - end



def checkcontent(con):
    name=[]
    l=[]
    for i in con:
        for j in column:
            l=wholelist[j]
            for k in range(len(l)):
                string=str(l[k])
                name=string.strip().split()
                if i in name:
                    print("BOT>> ",blogdata.loc[k,catt[0]])
            return("BOT>> Content Displayed")
    else:
        return("Sorry The Required Content is not avilable")



def result(content_list):
    if content_list[0]=='show':
       content_list.remove('show')
    elif content_list[0]=='Show':
       content_list.remove('Show')
    for i in content_list:
        if i in column:
            catt.append(i)
            content_list.remove(i)
    result=checkcontent(content_list)
    return(result)
    