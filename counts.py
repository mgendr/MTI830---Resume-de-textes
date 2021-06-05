# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:59:46 2021

@author: mathi
"""

import json
import gzip
import os
import sys
import argparse
#import panda as pd
import matplotlib.pyplot as plt
import re
# Library for boxplots
import seaborn as sns
import nltk

from nltk.corpus import stopwords
nltk.download('stopwords')

def readData(path,filename):
    json_obj_list=[]
    with open(os.path.join(path,filename),'r') as fin:
        for row in fin:
            json_obj_list.append(json.loads(row))
    return json_obj_list


def countData(split_type):
    file_names = os.listdir(os.path.join("data","train","g"))
    # reading one of the gz files.

    
    

    for file_name in file_names[:1] :
        print(file_name)
    #file_name = file_names[0]
        print("Reading file "+ file_name + " from "+ split_type+" split for cpc code " + cpc_code)
        
        with open(os.path.join("data","train","g"),'r') as fin:
            
            for row in fin:
                #print(row)
                
                json_obj = json.loads(row)
                count_character_abs.append(len(json_obj["abstract"]))
                count_character_des.append(len(json_obj["description"]))
                count_word_abs.append( json_obj["abstract"].count(" ") )
                count_word_des.append( json_obj["description"].count(" ")
                                      )
                for charac in json_obj["description"]:
                    if charac not in count_character.keys():
                        count_character[charac]=1
                    else :
                        count_character[charac]+=1              
                
                
                
                
                #print("Fields present in each of the json object:")
                #print(json_obj.keys())
                # uncomment to print the publication number, abstract and description
                #print(json_obj["publication_number"])
                # print(json_obj["abstract"])
                # print(json_obj["description"])
            #print(json_obj.keys())
count_character_abs=[]
count_character_des=[]
count_word_abs=[]
count_word_des=[]
count_character={}

def filterChars(path,filename,JSONlist):
    cachedstopwords = stopwords.words("english")
    if os.path.exists(path+'new_'+filename+'.txt')==True:
        os.remove(path+'new_'+filename+'.txt')
    new_f= open(os.path.join(path,'new_'+filename)+'.txt','a')
    for i in range(len(JSONlist)) :
        abstract = JSONlist[i]['abstract']
        description = JSONlist[i]['description']
            
        abstract1 = abstract.lower()
        description1 = description.lower()
            
        abstract2 = re.sub('[^a-zA-Z ]',' ',abstract1)
        description2 = re.sub('[^a-zA-Z ]',' ',description1)
            
        abstract3 = re.sub(r'(?:^| )\w(?:$| )', ' ', abstract2).strip()
        description3 = re.sub(r'(?:^| )\w(?:$| )', ' ', description2).strip()
            
        abstract4 = ' '.join([word for word in abstract3.split() if word not in cachedstopwords])
        description4 = ' '.join([word for word in description3.split() if word not in cachedstopwords])
            
        abstract5=re.sub(' +',' ',abstract4)
        description5=re.sub(' +',' ',description4)
            
        JSONlist[i]['abstract']=abstract5
        JSONlist[i]['description']=description5
        updatedJSON={"publication_number":JSONlist[i]['publication_number'],"abstract":abstract5,"description":description5}
        new_f.write(json.dumps(updatedJSON))
    print("Wrote file "+new_f.name)
    new_f.close()
    return JSONlist


# A remplacer par "train"  "val"   "test"
kind_data="test"

file_names = [file for file in os.listdir(os.path.join("data",kind_data,"g")) if ".txt" not in file]
for file_name in file_names:
    listJSON = readData(os.path.join("data",kind_data,"g"),file_name)
    JSONlist=filterChars(os.path.join("data",kind_data,"g"),file_name,listJSON)

     
#sns.boxplot(data=count_character_abs,fliersize=10) 
#plt.show()
#sns.boxplot(data=count_character_des,fliersize=10)
#plt.show() 
#sns.boxplot(data=count_word_abs,fliersize=10) 
#plt.show()
#sns.boxplot(data=count_word_des,fliersize=10)   
#plt.show()
#
#print(count_character)
