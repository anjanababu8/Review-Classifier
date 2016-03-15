import re

fo_cleaned = open("cleaned_data.txt","r") 
fo_vocabulary = open("vocabulary.txt","w")
dict = {}

for line in fo_cleaned:
	words = line.split()
        for word in words[1:]:
	   dict.setdefault(word, 0)
	   dict[word] = dict[word] + 1 

for word, count in dict.items():	
	if(count >= 1): 	# we have taken every words since we think that would benefit our model
		fo_vocabulary.write(word + "\n")
