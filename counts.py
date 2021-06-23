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


def countData():
    file_names = os.listdir(os.path.join("data","train","g"))
    # reading one of the gz files.
    for file_name in file_names :
        #print(file_name)
    
        print("Reading file "+ file_name + " from "+ "train"+" split for cpc code " + cpc_code)
        
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
                
count_character_abs=[]
count_character_des=[]
count_word_abs=[]
count_word_des=[]
count_character={}


countData()


sns.boxplot(data=count_character_abs,fliersize=10) 
plt.show()
sns.boxplot(data=count_character_des,fliersize=10)
plt.show() 
sns.boxplot(data=count_word_abs,fliersize=10) 
plt.show()
sns.boxplot(data=count_word_des,fliersize=10)   
plt.show()

print(count_character)
