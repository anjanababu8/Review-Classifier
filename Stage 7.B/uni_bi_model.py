import pickle
def trainingTheModel(training_set):

	# Returns an array of bigrams present in the vocabulary
	def getBigrams(fo):
		bigrams = []
		for word in fo:
			if len(word.split())==2:
				bigrams.append(word[:len(word)-1]) # to remove \n
		return bigrams
					
	# Get the Bag Of Words for + and -	
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
			      bwordList.setdefault(bigram,0)
			      bwordList[bigram] = bwordList[bigram] + 1
		return decCount(wordList, bwordList)		
		
	# Decrements the unigram count for which a bigram is present in the vocabulary
	def decCount(wordList, bwordList):
		for bi, bi_c in bwordList.items():
			if bi in bigramsInVocabulary:
				unigrams = bi.split()				
				wordList[unigrams[0]] = wordList[unigrams[0]] - bi_c
				wordList[unigrams[1]] = wordList[unigrams[1]] - bi_c	
		for uni, uni_c in wordList.items():
			if uni_c <0:
				wordList[uni] = 0
		return dict(wordList.items() + bwordList.items())	
		


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

	# Train a unigram-bigram naive bayes model
	def trainNaiveBayes():	
		fo_vocabulary = open("adv_vocabulary.txt","r")
		for line in fo_vocabulary:
			words = line.split()
			if(len(words) == 1):
				word = words[0]
				modelProb.setdefault(word,[0,0])   	
				
				# Unigram Probabilities
				if (word in BoW['+']):
					modelProb[word][0] = (BoW['+'][word]+1)*1.0 / (wordCount['+'] + vocabularyCount)
				else:
					modelProb[word][0] = 1.0 / (wordCount['+'] + vocabularyCount)
				if (word in BoW['-']):	
					modelProb[word][1] = (BoW['-'][word]+1)*1.0 / (wordCount['-'] + vocabularyCount) 
				else:
					modelProb[word][1] = 1.0 / (wordCount['-'] + vocabularyCount)
				
				

			if (len(words) == 2):
				word = words[0] + " " + words[1]
				modelProb.setdefault(word,[0,0])  
				if (word in BoW['+']):
					modelProb[word][0] = (BoW['+'][word]+1)*1.0 / (wordCount['+'] + vocabularyCount)
				else:
					modelProb[word][0] = 1.0 / (wordCount['+'] + vocabularyCount)

				if (word in BoW['-']):	
					modelProb[word][1] = (BoW['-'][word]+1)*1.0 / (wordCount['-'] + vocabularyCount) 
				else:
					modelProb[word][1] = 1.0 / (wordCount['-'] + vocabularyCount)
	
		return modelProb


	## DATA STRUCTURES and how it is populated
	modelProb = {}	# {Vocabulary_Word : [Probability in +, Probability in - review]} i.e w->[p+,p-]

	fo_vocabulary = open("adv_vocabulary.txt","r")
	bigramsInVocabulary = getBigrams(fo_vocabulary)	
	
	BoW = {'+': makeWordList('+'), '-': makeWordList('-')} # {'+' : {word:count....} }

	fo_vocabulary = open("adv_vocabulary.txt","r") # number of words in vocabulary
	vocabularyCount = countLines(fo_vocabulary)

	wordCount = {'+':countWords(BoW['+']), '-':countWords(BoW['-'])} # total occurences of words belonging to +/-ve review

	model =  trainNaiveBayes() # TRAIN THE MODEL : UNIGRAM-BIGRAM NAIVE BAYES MODEL
	
	pickle.dump(model, open("model.pickle", "wb" ) ) # SAVE THE MODEL
	# to make a human readable version of the model
	fo_model = open("model.txt","w")
	fo_model.write("WORD " + "	P+ " + "	P-" + '\n')
	for word,p in model.items():	
		fo_model.write(word + "		" + str(p[0]) + " 	" + str(p[1]) + '\n')

	return model

