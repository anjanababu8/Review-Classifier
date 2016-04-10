import pickle

def trainingTheModel(training_set):
	# Bag Of Words	
	def makeWordList(sign):		
		wordList = {}
		bwordList = {}
		for line in training_set:
			words = line.split()
			if(words and words[0] == sign):
				for w in words[1:]:
					wordList.setdefault(w,0)
					wordList[w] = wordList[w] + 1
			
			if(words and words[0] == sign):
			    for i in range(1,len(words)-1):
			      bigram = words[i] + ' ' + words[i+1]
			      wordList.setdefault(bigram,0)
			      wordList[bigram] = wordList[bigram] + 1
		return wordList

	# counts the number of lines in a file
	def countLines(file_ob):
		count = 0
		for line in file_ob:
			count = count + 1
		return count

	# counts the total number of words in a given wordlist
	def countWords(wordList):
		count = 0
		for word, wcount in wordList.items():
			count = count + wcount
		return count

	# Train a unigram naive bayes model
	def trainNaiveBayes():	
		fo_vocabulary = open("adv_vocabulary.txt","r")
		for line in fo_vocabulary:
			words = line.split()
			if(len(words) == 1):
				word = words[0]
				modelProbabilies.setdefault(word,[0,0])   	
				
				# Unigram Probabilities
				if (word in posDocWordList):
				 modelProbabilies[word][0] = (posDocWordList[word]+1)*1.0 / (wordCount[0] + vocabularyCount)
				else:
				 modelProbabilies[word][0] = 1.0 / (wordCount[0] + vocabularyCount)
				if (word in negDocWordList):	
				 modelProbabilies[word][1] = (negDocWordList[word]+1)*1.0 / (wordCount[1] + vocabularyCount) 
				else:
				 modelProbabilies[word][1] = 1.0 / (wordCount[1] + vocabularyCount)
				
				# Including START word and word STOP
				cb = ce = ncb = nce = 0
				for line in training_set:
					w = line.split()
					if(w[0] == '+' and len(w)>1):
						if(w[1] == word):
							cb = cb + 1
						if(w[len(w)-1] == word):
							ce = ce + 1	
					elif(w[0] == '-' and len(w)>1):
						if(w[1] == word):
							ncb = ncb + 1
						if(w[len(w)-1] == word):
							nce = nce + 1	

				modelProbabilies.setdefault('START ' + word,[0,0])
				modelProbabilies.setdefault(word +' STOP',[0,0])   	
   	
				modelProbabilies['START ' + word][0] = (cb+1)*1.0 / (wordCount[0] + vocabularyCount)
				modelProbabilies['START ' + word][1] = (ncb+1)*1.0 / (wordCount[1] + vocabularyCount)

				modelProbabilies[word + ' STOP'][0] = (ce+1)*1.0 / (wordCount[0] + vocabularyCount)
				modelProbabilies[word + ' STOP'][1] = (nce+1)*1.0/ (wordCount[1] + vocabularyCount)		

			if (len(words) == 2):
				word = words[0] + " " + words[1]
				modelProbabilies.setdefault(word,[0,0])  
				if (word in posDocWordList):
					modelProbabilies[word][0] = (posDocWordList[word]+1)*1.0 / (wordCount[0] + vocabularyCount)
				else:
					modelProbabilies[word][0] = 1.0 / (wordCount[0] + vocabularyCount)

				if (word in negDocWordList):	
					modelProbabilies[word][1] = (negDocWordList[word]+1)*1.0 / (wordCount[1] + vocabularyCount) 
				else:
					modelProbabilies[word][1] = 1.0 / (wordCount[1] + vocabularyCount)
	


		return modelProbabilies


	## DATA STRUCTURES and how it is populated
	modelProbabilies = {}	# {Vocabulary_Word : [Probability in +, Probability in - review]} i.e w->[p+,p-]
	
	posDocWordList = makeWordList('+') # word:count in +ve Reviews  
	negDocWordList = makeWordList('-') # word:count in -ve Reviews

	fo_vocabulary = open("adv_vocabulary.txt","r") # number of words in vocabulary
	global vocabularyCount
	vocabularyCount = countLines(fo_vocabulary) + 2

	global wordCount
	wordCount = [countWords(posDocWordList),countWords(negDocWordList)] # total words belonging to +/-ve review

	model = trainNaiveBayes() # TRAIN THE MODEL : UNIGRAM NAIVE BAYES MODEL
	
	return model
	

