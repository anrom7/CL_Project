''' Барабах Христина, ПРЛс-11'''
# Відкриваю файли із позитивними, негативними і нейтральними словами
>>> f1= open('C:/Users/TINA/Desktop/zachust/positive.txt')
>>> f2= open('C:/Users/TINA/Desktop/zachust/negative.txt')
>>> f3= open('C:/Users/TINA/Desktop/zachust/neutral.txt')
# Підраховую кількість позитивних слів у файлі
>>> pos_w=[]
>>> for i in f1.readlines():
	pos_w.append(i[:-1])

	
>>> print ('pos_w', len(pos_w))
('pos_w', 211)

# Підраховую кількість негативних слів у файлі
>>> neg_w=[]
>>> for i in f2.readlines():
	neg_w.append(i[:-1])

	
>>> print ('neg_w', len(neg_w))
('neg_w', 131)

# Підраховую кількість нейтральних слів у файлі
>>> neu_w=[]
>>> for i in f3.readlines():
	neu_w.append(i[:-1])

	
>>> print ('neu_w', len(neu_w))
('neu_w', 739)

#Загальна кількісь усіх слів у файлах(позитивні+негативні+нейтральні)
>>> f4=open('C:/Users/TINA/Desktop/zachust/list.txt')
>>> list_suma =[]
>>> for i in f4.readlines():
	list_suma.append(i[:-1])

	
>>> print ('list_suma', len(list_suma))
('list_suma', 1081)
#Підраховую кількість позитивних слів у словнику
>>> rez_pos=[]
>>> with open ('C:/Users/TINA/Desktop/zachust/generated_dic.txt') as f:
	for i in f.readlines():
		s=i.split(',')
		if s[-1].strip() == '1':
			rez_pos.append(s[0])

			
>>> print ('rez_pos', len (rez_pos))
('rez_pos', 1524)
# Підраховую кількість негативних слів у словнику
>>> rez_neg=[]
>>> with open ('C:/Users/TINA/Desktop/zachust/generated_dic.txt') as f:
	for i in f.readlines():
		s=i.split(',')
		if s[-1].strip() == '-1':
			rez_neg.append(s[0])

			
>>> print ('rez_neg', len (rez_neg))
('rez_neg', 3113)

#Підраховую кількість нейтральних слів у словнику
>>> rez_neu=[]
>>> with open ('C:/Users/TINA/Desktop/zachust/generated_dic.txt') as f:
	for i in f.readlines():
		s=i.split(',')
		if s[-1].strip() == '0':
			rez_neu.append(s[0])

			
>>> print ('rez_neu', len (rez_neu))
('rez_neu', 211)
# Сума усіх слів у словнику (позитивні+негативні + нейтральні)
>>> Suma_dic=[]
>>> with open ('C:/Users/TINA/Desktop/zachust/generated_dic.txt') as f:
	for i in f.readlines():
		Suma_dic.append(i[:-1])

		
>>> print ('Suma_dictionary', len(Suma_dic))
('Suma_dictionary', 46417)

#Точність позитивних слів
>>> print ("Tochnist_pos", len(pos_w)/float(len(rez_pos)))
('Tochnist_pos', 0.04550355833513047)
#Точність негативних слів
>>> print ("Tochnist_neg", len(neg_w)/float(len(rez_neg)))
('Tochnist_neg', 0.04136406694032207)
#Точність нейтральних слів
>>> print ("Tochnist_neu", len(neu_w)/float(len(rez_neu)))
('Tochnist_neu', 56.84615384615385)
#Повнота позитивних слів
>>> print("Povnota_pos", len(pos_w)/float(len(list_suma)))
('Povnota_pos', 0.19518963922294172)
#Повнота негативних слів
>>> print("Povnota_neg", len(neg_w)/float(len(list_suma)))
('Povnota_pos', 0.1211840888066605)
#Повнота нейтральних слів
>>> print("Povnota_neu", len(neu_w)/float(len(list_suma)))
('Povnota_pos', 0.6836262719703978)
#Повнота усіх слів
>>> print('Povnota', len(list_suma)/float(len(Suma_dic)))
('Povnota_pos', 0.023288881228860116)
