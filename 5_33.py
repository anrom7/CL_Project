import nltk
pos=nltk.defaultdict(dict) 
brown_tagged=nltk.corpus.brown.tagged_words()
for ((w1,t1),(w2,t2)) in nltk.ibigrams(brown_tagged):
    print w1+":", t1,[t2][:50]

#w1,w2 - dictionaries
#t1,t2 - tags
