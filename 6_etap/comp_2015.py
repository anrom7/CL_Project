# Відкрити файл з позитивними, негативними і нейтральними словами
f1=open('E:/Files/6_etap/Bulavkina_seedwords.txt')
pos_w=[]
# Збереження позитивних слів у список
for i in f1.readlines():
	pos_w.append(i[:-1])
# Вивід на екран кількість позитивних слів	
print ('pos', len(pos_w))
neg_w=[]
# Збереження негативних слів у список
for i in f1.readlines():
	neg_w.append(i[:-1])
# Вивід на екран кількість негативних слів
print ('neg', len(neg_w))
neut_w=[]
# Збереження нейтральних слів у список
for i in f1.readlines():
	neut_w.append(i[:-1])
# Вивід на екран кількість нейтральних слів
print ('neut', len(neut_w))
rez=[]
# Відкрити файли зі згенерованим словником
f2=open('E:/Files/6_etap/Bulavkina_dic.csv')
# Збереження у список слів та їх тональності зі словника, якщо це слово
# є у списку позитивних слів 
for i in f2.readlines():
	#print (i.split(',')[+])
	if i.split(',')[0] in pos_w: #якщо слово є серед позитивних слів, то воно його рахує
		#print (i.split(',')[0])
		rez.append(i.split(',')[:2])
# Вивід на екран кількості слів зі словника, які є серед позитивних слів
print ('rez', len(rez))
# Вивід на екран відношення кількості слів зі словника
# до кількості позитивних слів
print ('Recall_pos', (len(rez)-len(pos_w))/len(pos_w))
# Відкриття і запис у файл слів зі словника, які є серед позитивних слів
z=open('E:/Files/6_etap/pos_domen_rez.txt','w')
for i in rez:
	z.write(str(i)+'\n')
z.close()
rez=[]
# Відкрити файли зі згенерованим словником
f2=open('E:/Files/6_etap/Bulavkina_dic.csv')
# Збереження у список слів та їх тональності зі словника, якщо це слово
# є у списку негативних слів 
for i in f2.readlines():
	#print (i.split(',')[0])
	if i.split(',')[0] in neg_w:
		#print (i.split(',')[0])
		rez.append(i.split(',')[:2])
# Вивід на екран кількості слів зі словника, які є серед негативних слів		
print ('rez', len(rez))
# Вивід на екран відношення кількості слів зі словника
# до кількості негативних слів
print ('Recall_neg', (len(rez)-len(neg_w))/len(neg_w))
# Відкриття і запис у файл слів зі словника, які є серед негативних слів
z=open('E:/Files/6_etap/neg_domen_rez.txt','w')
for i in rez:
	z.write(str(i)+'\n')
z.close()
# Відкрити файли зі згенерованим словником
f2=open('E:/Files/6_etap/Bulavkina_dic.csv')
# Збереження у список слів та їх тональності зі словника, якщо це слово
# є у списку нейтральних слів 
for i in f2.readlines():
	#print (i.split(',')[0])
	if i.split(',')[0] in neut_w:
		#print (i.split(',')[0])
		rez.append(i.split(',')[:2])
# Вивід на екран кількості слів зі словника, які є серед нейтральних слів		
print ('rez', len(rez))
# Вивід на екран відношення кількості слів зі словника
# до кількості нейтральних слів
print ('Recall_neut', (len(rez)-len(neut_w))/len(neut_w))
# Відкриття і запис у файл слів зі словника, які є серед нейтральних слів
z=open('E:/Files/6_etap/neut_domen_rez.txt','w')
for i in rez:
	z.write(str(i)+'\n')
z.close()

		
	
