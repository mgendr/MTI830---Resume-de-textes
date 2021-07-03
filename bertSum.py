# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 18:23:47 2021

@author: mathi
"""
import json
import os



def readData(path):
    json_obj_list=[]
    with open(os.path.join(path,'new_data000000000000.txt'),'r') as fin:
        for row in fin:
            json_obj_list.append(json.loads(row))
    return json_obj_list


file_names = [file for file in os.listdir(os.path.join("data","val","g"))]
for file_name in file_names[:1]:
    listJSON = readData(os.path.join("data","val","g"))
#from summarizer import Summarizer
#model = Summarizer()
#result = model(get_corona_summary, min_length=20)
#summary = "".join(result)
#print(summary)