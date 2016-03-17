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
	
# Text preprocessing - tokenise, normalise and stopword removal
for line in fo_data:
	
	words =  re.sub('[,.!]',' ', line).split() # tokenise 

	fo_cleaned.write(words[0] + " ")
        
	for word in words[1:]:
	   word = re.sub('[^A-Za-z]', '', word)
	   word = word.lower() # normalise (converted to lower case)
	   if(word and not STOPWORD(word) and len(word)>1):
		fo_cleaned.write(word + " ")
	fo_cleaned.write("\n")
