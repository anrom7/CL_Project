# -*- coding: cp1251 -*-
import codecs, re
with codecs.open("C:/CL_Project/2015/Savkiv_seedwords.txt", 'r', encoding='utf-8') as seed_file: 
	 seed_l = seed_file.readlines()
	 seed_l = [x.replace("\r\n", "") for x in seed_l]
	 print("Count of Seed_words  {count}".format(count=len(seed_l))) #вивід загальної кількості слів Seed_words 


with codecs.open("C:/CL_Project/2015/dic.csv", 'r', encoding='utf-8') as dic_file:
	dic_l = dic_file.readlines()
	dic_l = [x.replace("\r\n", "") for x in dic_l]
	print("Count of Dic_words  {count}".format(count=len(dic_l)))#вивід загальної кількості слів dic_words
tp=[]
tp1=[]
tp2=[]
tp3=[]
with codecs.open("C:/CL_Project/2015/Savkiv_seedwords.txt", 'r', encoding='utf-8') as seed_file: 
    for i in seed_file.readlines():
        s=i.split(',')
        with codecs.open("C:/CL_Project/2015/dic.csv", 'r', encoding='utf-8') as dic_file:
            for j in dic_file.readlines():
                d=j.split(',')
                if (s[0]==d[0]) and (s[1].strip()=='1') and (d[1].strip()==('+')):
                    tp1.append(i.split(',')[:2])
                if (s[0]==d[0]) and (s[1].strip()=='-1') and (d[1].strip()==('-')):
                    tp2.append(i.split(',')[:2])
                if (s[0]==d[0]) and (s[1].strip()=='0') and (d[1].strip()==('0')):
                    tp3.append(i.split(',')[:2])
                    
                    
    
#Recall,  which  indicates  how  many  of  the  relevant  items  that  we  identified,  is TP/(TP+FN),
#where TP+FN=count(len(seed_l))
print ("Recall =  {count}".format(count=float((len(tp1)+(len(tp2))+(len(tp3))))/float(len(seed_l))))
  
#підрахунок слів у згенерованому словнику, які неправильно промарковані
incorrect_dic=[]
with codecs.open("C:/CL_Project/2015/dic.csv", 'r', encoding='utf-8') as dic_file:
    for j in dic_file.readlines():
        d=j.split(',')
        if (d[1].strip()=='A') or (d[1].strip()==('U')):
            incorrect_dic.append(i.split(',')[:2])


#Precision,  which indicates how many of the items that we identified were relevant,
#is TP/(TP+FP), where TP+FN=count of dic_l len without 'a' and 'u'
print ("Precision = {count}".format(count=float((len(tp1)+(len(tp2))+(len(tp3))))/(float(len(dic_l))-len(incorrect_dic))))
