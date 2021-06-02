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
def readData(input_path,split_type,cpc_code):
    file_names = os.listdir(os.path.join(input_path,split_type,cpc_code))
    # reading one of the gz files.

    
    

    for file_name in file_names[:6] :
        print(file_name)
    #file_name = file_names[0]
        print("Reading file "+ file_name + " from "+ split_type+" split for cpc code " + cpc_code)
        
        with open(os.path.join(input_path,split_type,cpc_code,file_name),'r') as fin:
            
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
                ###Afin de compter les mots on va compter les espaces dans une 1ère approche
                
                
                
                
                
                
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

def filterChars(input_path,split_type,cpc_code):
    file_names = os.listdir(os.path.join(input_path,split_type,cpc_code))
    # reading one of the gz files.
    cachedstopwords = stopwords.words("english")
    for file_name in file_names[:2] :
        print(file_name)
    #file_name = file_names[0]
        print("Reading file "+ file_name + " from "+ split_type+" split for cpc code " + cpc_code)
        
        f = open(os.path.join(input_path,split_type,cpc_code,file_name),'r')

        regex = re.compile('[^a-zA-Z ]')
        content = f.read().lower()
        new_f= open(os.path.join(input_path,split_type,cpc_code,'new_'+file_name)+'.txt','w+')
        filtered_content = regex.sub(' ',content)
        filtered_content2 = re.sub(r'(?:^| )\w(?:$| )', ' ', filtered_content).strip()
        removedStopwords = ' '.join([word for word in filtered_content2.split() if word not in cachedstopwords])
        stripped_content=re.sub(' +',' ',removedStopwords)

        new_f.write(stripped_content)
        print("Wrote file "+new_f.name)
        f.close()
        new_f.close()
        
filterChars("data","train","g")

     
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
