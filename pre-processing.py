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
import numpy as np
# Library for boxplots
import seaborn as sns
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
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

def createStemmedFiles(path,filename, JSONlist):
    if os.path.exists(path+'stemmed_'+filename)==True:
        os.remove(path+'stemmed_'+filename)
    new_f= open(os.path.join(path,'stemmed_'+filename),'a')
    for i in range(len(JSONlist)) :
        abstract = JSONlist[i]['abstract']
        description = JSONlist[i]['description']
        porter=PorterStemmer()
        abstract2=' '.join(porter.stem(token) for token in word_tokenize(abstract));
            
        porter2=PorterStemmer()
        description2=' '.join(porter2.stem(token) for token in word_tokenize(description));
        JSONlist[i]['abstract']=abstract2
        JSONlist[i]['description']=description2
        updatedJSON={"publication_number":JSONlist[i]['publication_number'],"abstract":abstract2,"description":description2}
        new_f.write(json.dumps(updatedJSON))
    print("Wrote file "+new_f.name)   
    new_f.close()
    
def addLineReturn(path,filename):
    f=open(os.path.join(path,file_name2),'r')
    text = f.read().replace('}{"publication_number"','}\n{"publication_number"').encode("utf8")
    f.close()
    f2=open(os.path.join(os.path.join("data",kind_data,"g"),file_name2),'wb')
    f2.write(text)
    f2.close()
    print("Updated file "+f2.name)
    
def getCounts():
    abstract_word_count = []
    description_word_count = []
    file_names = [file for file in os.listdir(os.path.join("data","test","g")) if ".txt" in file]
    for file_name in file_names: 
        listJSON = readData(os.path.join("data","test","g"),file_name)
        for i in range(len(listJSON)) :
            abstract = listJSON[i]['abstract']
            description = listJSON[i]['description']
            
            abstract_word_count.append(len(abstract.split()))
            description_word_count.append(len(description.split()))
    file_names2 = [file for file in os.listdir(os.path.join("data","train","g")) if ".txt" in file]
    for file_name in file_names2: 
        listJSON = readData(os.path.join("data","train","g"),file_name)
        for i in range(len(listJSON)) :
            abstract = listJSON[i]['abstract']
            description = listJSON[i]['description']
            
            abstract_word_count.append(len(abstract.split()))
            description_word_count.append(len(description.split()))
    file_names3 = [file for file in os.listdir(os.path.join("data","val","g")) if ".txt" in file]
    for file_name in file_names3: 
        listJSON = readData(os.path.join("data","val","g"),file_name)
        for i in range(len(listJSON)) :
            abstract = listJSON[i]['abstract']
            description = listJSON[i]['description']
            
            abstract_word_count.append(len(abstract.split()))
            description_word_count.append(len(description.split()))
    return abstract_word_count,description_word_count

def createNoOutliersFiles(path,filename, JSONlist,minAbs,maxAbs,minDesc,maxDesc):
    if os.path.exists(path+'nooutliers_'+filename)==True:
        os.remove(path+'nooutliers_'+filename)
    new_f= open(os.path.join(path,'nooutliers_'+filename),'a')
    
    for i in range(len(JSONlist)) :
        if len(JSONlist[i]['abstract'].split())>minAbs and len(JSONlist[i]['abstract'].split())<maxAbs and len(JSONlist[i]['description'].split())>minDesc and len(JSONlist[i]['description'].split())<maxDesc:
            updatedJSON={"publication_number":JSONlist[i]['publication_number'],"abstract":JSONlist[i]['abstract'],"description":JSONlist[i]['description']}
            new_f.write(json.dumps(updatedJSON))
    print("Wrote file "+new_f.name)   
    new_f.close()
# A remplacer par "train"  "val"   "test"
kind_data="train"

#%%
#file_names = [file for file in os.listdir(os.path.join("data",kind_data,"g")) if ".txt" not in file]
#for file_name in file_names:
#    listJSON = readData(os.path.join("data",kind_data,"g"),file_name)
#    JSONlist=filterChars(os.path.join("data",kind_data,"g"),file_name,listJSON)
#
##f=open(os.path.join(os.path.join("data",kind_data,"g"),'data000000000000'),'r',encoding="utf8")
##text =f.read()
##print(text)
#
#file_names2 = [file for file in os.listdir(os.path.join("data",kind_data,"g")) if file.endswith('.txt')] 
#for file_name2 in file_names2:
#    addLineReturn(os.path.join("data",kind_data,"g"),file_name2)

absCount, descCount = getCounts()
print("90 Percentile ABSTRACT "+str(np.percentile(absCount,90)))
print("95 Percentile ABSTRACT "+str(np.percentile(absCount,95)))
print("99 Percentile ABSTRACT "+str(np.percentile(absCount,99)))
print("Max ABSTRACT "+str(max(absCount)))
    
print("\n90 Percentile DESCRIPTION "+str(np.percentile(descCount,90)))
print("95 Percentile DESCRIPTION "+str(np.percentile(descCount,95)))
print("99 Percentile DESCRIPTION "+str(np.percentile(descCount,99)))
print("Max DESCRIPTION "+str(max(descCount)))
#%%
    
#os.makedirs("stemmed", exist_ok=True)
#for kind_data in ["test"]:
#    name_folder0 = "stemmed/"+kind_data
#    name_folder = "stemmed/"+kind_data+"/g"
#    os.makedirs(name_folder0, exist_ok=True)
#    os.makedirs(name_folder, exist_ok=True)
#    
#    file_names = [file for file in os.listdir(os.path.join("data",kind_data,"g")) if ".txt" in file]
#    for i in range(len(file_names)) :
#        file_name=file_names[i]
#        listJSON = readData(os.path.join("data",kind_data,"g"),file_name) 
#        createStemmedFiles(name_folder+"/",file_name.strip('new_'),listJSON)

os.makedirs("noOutliers", exist_ok=True)
for kind_data in ["val"]:
    name_folder0 = "noOutliers/"+kind_data
    name_folder = "noOutliers/"+kind_data+"/g"
    os.makedirs(name_folder0, exist_ok=True)
    os.makedirs(name_folder, exist_ok=True)
    
    file_names = [file for file in os.listdir(os.path.join("data",kind_data,"g")) if ".txt" in file]
    for i in range(len(file_names)) :
        file_name=file_names[i]
        listJSON = readData(os.path.join("data",kind_data,"g"),file_name) 
        createNoOutliersFiles(name_folder+"/",file_name.strip('new_'),listJSON,np.percentile(absCount,5),np.percentile(absCount,95),np.percentile(descCount,5),np.percentile(descCount,95))
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
