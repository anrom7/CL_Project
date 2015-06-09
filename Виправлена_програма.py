''' Barabakh Khrystyna'''
# open all files with positive, negative and neutral words
f1= open('F:/zachust/positive.txt')
f2= open('F:/zachust/negative.txt')
f3= open('F:/zachust/neutral.txt')
# count all words in file with positive words
pos_w=[]
for i in f1.readlines():
        pos_w.append(i[:-1])

        
print ('pos_w', len(pos_w))
('pos_w', 211)

#  count all words in file with negative words
neg_w=[]
for i in f2.readlines():
        neg_w.append(i[:-1])

        
print ('neg_w', len(neg_w))
('neg_w', 131)

#  count all words in file with neutral words
neu_w=[]
for i in f3.readlines():
        neu_w.append(i[:-1])

        
print ('neu_w', len(neu_w))
('neu_w', 739)

# count all word in file
f4=open('F:/zachust/list.txt')
list_suma =[]
for i in f4.readlines():
        list_suma.append(i[:-1])

        
print ('list_suma', len(list_suma))
('list_suma', 108)
# count all positive words in generated dictionary
rez_pos=[]
with open ('F:/zachust/generated_dic.txt') as f:
        for i in f.readlines():
                s=i.split(',')
                if s[-5].strip() == '+':
                        rez_pos.append(s[0])

                        
print ('rez_pos', len (rez_pos))

# count all negative words in generated dictionary
rez_neg=[]
with open ('F:/zachust/generated_dic.txt') as f:
        for i in f.readlines():
                s=i.split(',')
                if s[-5].strip() == '-':
                        rez_neg.append(s[0])

                        
print ('rez_neg', len (rez_neg))


#count all neutral words in generated dictionary
rez_neu=[]
with open ('F:/zachust/generated_dic.txt') as f:
        for i in f.readlines():
                s=i.split(',')
                if s[-5].strip() == '0':
                        rez_neu.append(s[0])

                        
print ('rez_neu', len (rez_neu))


# count all words in generated dictionary
Suma_dic=[]
with open ('F:/zachust/generated_dic.txt') as f:
        for i in f.readlines():
                Suma_dic.append(i[:-1])

                
print ('Suma_dictionary', len(Suma_dic))
('Suma_dictionary', 46417)

# count all U-words in generated dictionary
words_without_U=[]
with open ('F:/zachust/generated_dic.txt') as f:
        for i in f.readlines():
                s=i.split(',')
                if s[-5].strip() == 'U':
                        words_without_U.append(s[0])

                        
print('words_without_U', len(words_without_U))
('words_without_U', 6885)

# count all A-words in generated dictionary
words_without_A=[]
with open ('F:/zachust/generated_dic.txt') as f:
        for i in f.readlines():
                s=i.split(',')
                if s[-5].strip() == 'A':
                        words_without_A.append(s[0])

                        
print('words_without_A', len(words_without_A))
('words_without_A', 2023)

# count all U-words + A-words 
Suma_wTH=[]
Suma_wTH= len(words_without_A)+len(words_without_U)
print('Suma_A_and_U',Suma_wTH)
('Suma_A_and_U', 8908)

#count suma without all U-words + A-words 
c=[]
Suma_S=[]
a=len(Suma_dic)
Suma_S= a - Suma_wTH
print ('Suma without all U-words + A-words ', Suma_S)
#('Suma without all U-words + A-words ', 37509)

# accuracy of positive words
print ("Tochnist_pos", len(pos_w)/float(len(rez_pos)))


# accuracy of negative words
print ("Tochnist_neg", len(neg_w)/float(len(rez_neg)))


# accuracy of neutral words
print ("Tochnist_neu", len(neu_w)/float(len(rez_neu)))


# completeness of positive words
print("Povnota_pos", len(pos_w)/float(len(list_suma)))


# completeness of negative words
print("Povnota_neg", len(neg_w)/float(len(list_suma)))


# completeness of neutral words
print("Povnota_neu", len(neu_w)/float(len(list_suma)))


# completeness of dictionary
print('Povnota', len(list_suma)/float(Suma_S))
