import codecs

# Відкрити файли з позитивними  словами
with codecs.open("positive.txt", 'r', encoding='utf-8') as positive_file:
    # Збереження позитивних слів у список
    positive_list = positive_file.readlines()
    positive_list = [x.replace("\r\n", "") for x in positive_list]
    # Вивід на екран кількість позитивних слів
    print("Positive words count {count}".format(count=len(positive_list)))

# Відкрити файли з позитивними  словами
with codecs.open("negative.txt", 'r', encoding='utf-8') as negative_file:
    # Збереження негативних слів у список
    negative_list = negative_file.readlines()
    negative_list = [x.replace("\r\n", "") for x in negative_list]
    # Вивід на екран кількість негативних слів
    print("Negative words count {count}".format(count=len(negative_list)))

pos_words_in_dict = []
# Відкрити файл зі згенерованим словником та вичитати у список
with codecs.open("rez_domen5.txt", 'r', encoding='utf-8') as dictionary:
    dict_list = dictionary.readlines()
    dict_list = [x.replace("\r\n", "") for x in dict_list]
    # Збереження у список слів та їх тональності зі словника, якщо це слово
    # є у списку позитивних слів
    for line in dict_list:
        if line.split(',')[0] in positive_list:
            pos_words_in_dict.append(line.split(',')[:2])
# Вивід на екран кількості слів зі словника, які є серед позитивних слів
print("Positive words in dictionary {count}".format(count=len(pos_words_in_dict)))

# Відкриття і запис у файл слів зі словника, які є серед позитивних слів
with codecs.open("pos_domen_rez5.txt", 'w', encoding='utf-8') as pos_dict_file:
    for item in pos_words_in_dict:
        pos_dict_file.write('\r\n'.join(reversed(item)))

# Збереження у список слів та їх тональності зі словника, якщо це слово
# є у списку негативних слів
neg_words_in_dict = []
for line in dict_list:
    if line.split(',')[0] in negative_list:
        neg_words_in_dict.append(line.split(',')[:2])

# Вивід на екран кількості слів зі словника, які є серед негативних слів
print("Negative words in dictionary {count}".format(count=len(neg_words_in_dict)))

# Відкриття і запис у файл слів зі словника, які є серед негативних слів
with codecs.open("neg_domen_rez5.txt", 'w', encoding='utf-8') as neg_dict_file:
    for item in neg_words_in_dict:
        neg_dict_file.write('\r\n'.join(reversed(item)))

# Збереження у список слів та їх тональності зі словника, якщо цього
# слова нема у списку позитивних і негативних, типу воно нейтральне
neutral_words_in_dict = []
for line in dict_list:
    if line.split(',')[0] not in negative_list and line.split(',')[0] not in positive_list:
        neutral_words_in_dict.append(line.split(',')[:2])

# Вивід на екран кількості слів зі словника, які є нейтральні
print("Neutral words in dictionary {count}".format(count=len(neutral_words_in_dict)-1))

# Вивід на екран відношення кількості слів зі словника
# до кількості нейтральних, негативних і позитивних слів
print("Ratio neutral words in dictionary - {ratio}".format(
    ratio=float(len(neutral_words_in_dict) + len(neg_words_in_dict) + len(pos_words_in_dict)) / float(len(dict_list) - 1)))

# Відкриття і запис у файл нейтральних слів зі словника
with codecs.open("neutral_domen_rez5.txt", 'w', encoding='utf-8') as neutral_dict_file:
    for item in neutral_words_in_dict:
        neutral_dict_file.write('\r\n'.join(reversed(item)))
