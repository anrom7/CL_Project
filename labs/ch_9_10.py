import nltk
fs1 = nltk.FeatStruct(Category="Chas")
fs2 = nltk.FeatStruct(Category="Chas", Other_Category='Misce')# Defining the features
print fs1.unify(fs2)# Unifying the features
