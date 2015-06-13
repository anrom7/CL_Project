# -*- coding: cp1251 -*-
import codecs, re
with codecs.open("C:/CL_Project/VI/Rurych_seedwords.txt", 'r', encoding='utf-8') as seed_file: 
	 seed_list = seed_file.readlines()
	 seed_list = [x.replace("\r\n", "") for x in seed_list]
	 print("Seed_words count {count}".format(count=len(seed_list))) #вивід загальної кількості слів Seed_words 


with codecs.open("C:/CL_Project/VI/Rurych_dic.txt", 'r', encoding='utf-8') as dic_file:
	dic_list = dic_file.readlines()
	dic_list = [x.replace("\r\n", "") for x in dic_list]
	print("Dic_words count {count}".format(count=len(dic_list)))#вивід загальної кількості слів dic_words
tp=[]
tp1=[]
tp2=[]
tp3=[]
with codecs.open("C:/CL_Project/VI/Rurych_seedwords.txt", 'r', encoding='utf-8') as seed_file: 
    for i in seed_file.readlines():
        s=i.split(',')
        with codecs.open("C:/CL_Project/VI/Rurych_dic.txt", 'r', encoding='utf-8') as dic_file:
            for j in dic_file.readlines():
                d=j.split(',')
                if (s[0]==d[0]) and (s[1].strip()=='1') and (d[1].strip()==('+')):
                    tp1.append(i.split(',')[:2])
                if (s[0]==d[0]) and (s[1].strip()=='-1') and (d[1].strip()==('-')):
                    tp2.append(i.split(',')[:2])
                if (s[0]==d[0]) and (s[1].strip()=='0') and (d[1].strip()==('0')):
                    tp3.append(i.split(',')[:2])
                    
                    
    print("tp1 {count}".format(count=len(tp1)))
    print("tp2 {count}".format(count=len(tp2)))
    print("tp3 {count}".format(count=len(tp3)))

tp=len(tp1)+len(tp2)+len(tp3) #кількість TP
seed=''.join(seed_list)
seed_len=len(seed)

print("TD = {count}".format(count=tp))

#Recall,  which  indicates  how  many  of  the  relevant  items  that  we  identified,  is TP/(TP+FN),
#where TP+FN=count(len(seed_list))
print ("Recall =  {count}".format(count=tp/seed_len))

#підрахунок слів у згенерованому словнику, які неправильно промарковані
incorrect_dic=[]
with codecs.open("C:/CL_Project/VI/Rurych_dic.txt", 'r', encoding='utf-8') as dic_file:
    for j in dic_file.readlines():
        d=j.split(',')
        if (d[1].strip()=='A') or (d[1].strip()==('U')):
            incorrect_dic.append(i.split(',')[:2])
au=len(incorrect_dic)
print 'incorrect_dic =', au #FP=len(dic_list)-len(incorrect_dic)-tp


#Precision,  which indicates how many of the items that we identified were relevant,
#is TP/(TP+FP), where TP+FN=count of dic_list len without 'a' and 'u'
print 'Precision =', ((len(tp1)+len(tp2)+len(tp3))/(len(dic_list)-len(incorrect_dic)))
       

            
            
        
    
        
        
    





