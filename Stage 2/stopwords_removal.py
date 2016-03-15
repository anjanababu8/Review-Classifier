# The program parses the reviews in the file data.txt and create a file cleaned_data.txt 
# Cleaning process includes removal of stopwords (mentioned in stopwords.txt) and 
# removal of non-alphabetic characters

import re

fo_data = open("data.txt","r") # Open the data.txt to read the reviews. 
fo_cleaned = open("cleaned_data.txt","w") # Open the cleaned_data.txt to write back the cleaned reviews.

# Checks whether the argument is a stopword and returns True if it is stopword else False
def STOPWORD(word):
	fo_stopword = open("stopwords.txt","r")
	for stopword in fo_stopword:
		if (stopword.strip() == word.strip()):
			return True	
		
	return False
	
	

for line in fo_data:
	words = line.split()
	fo_cleaned.write(words[0] + " ")
        for word in words[1:]:
	   cropped_word = re.sub('[^A-Za-z]', ' ', word)
	   lower_word = cropped_word.lower().replace(" ", "")
	   if(lower_word and not STOPWORD(lower_word)):
		fo_cleaned.write(lower_word + " ")
	fo_cleaned.write("\n")
