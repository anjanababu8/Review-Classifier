import math
import uni_bi_model  # Module made in Step 4 included to make the model

# Counts the number of +/- ve reviews in the corpus 	
def countReviews(corpus,sign):
	count = 0
	for review in corpus:
		if(review[0] == sign):
			count = count + 1
	return count	

def evaluation():
	accuracy = {'UB' : [], 'B': []}

	for i in range(10): # 10 fold evaluation		
		fo_data = open("cleaned_data.txt",'r')
		corpus = fo_data.readlines()		
		test_set = corpus[i*60:(i+1)*60]
		
		j = 0
		training_set = []
		for r in corpus:
			if j not in range(i*60,(i+1)*60):
				training_set.append(r)
			j = j + 1
		
		modelProb = uni_bi_model.trainingTheModel(training_set) # Train the model using the new training_set

		correct = {'UB':0,'B':0}
		countOfReviews  = {'+' : countReviews(training_set, '+'), '-' : countReviews(training_set, '-')} # 30, 30
		for review in test_set:
			prior = {'+': math.log(1.0*countOfReviews['+']/len(training_set)),
				 '-': math.log(1.0*countOfReviews['-']/len(training_set))}
			
			# Initialise with the Prior Probabilities : 2 VAR for 2 Model evaluations
			sentProb = {'UB' : {'+': prior['+'], '-':prior['-']},
				    'B' :  {'+': prior['+'], '-':prior['-']}}  
				
			words = review.split()
			if(len(words)<2):
				continue		


		        for i in range(1,len(words)-1): # iter from 1 to n-2 [0,1,...... n-2,n-1]
		           bigram = words[i] + ' ' + words[i+1]
			   uni_1, uni_2 = words[i], words[i+1] 

			   # EVALUATION : 
			   # (UB) Considering Both Unigram and Bigram features
			   # (B) Considering only Bigram features
			   if bigram in modelProb:
			     sentProb['UB']['+'] = sentProb['UB']['+'] + math.log(modelProb[bigram][0])
			     sentProb['UB']['-'] = sentProb['UB']['-'] + math.log(modelProb[bigram][1])
 			     sentProb['B']['+'] = sentProb['B']['+'] +  math.log(modelProb[bigram][0])
 			     sentProb['B']['-'] = sentProb['B']['-'] +  math.log(modelProb[bigram][1])
			   
			   else: # Bigram not in vocabulary as its count<2 then consider its unigram probability
			     sentProb['UB']['+'] = sentProb['UB']['+'] + math.log(modelProb[uni_1][0])
			     sentProb['UB']['-'] = sentProb['UB']['-'] + math.log(modelProb[uni_1][1])
			     if i == len(words)-2: # Take the last word also
				sentProb['UB']['+'] = sentProb['UB']['+'] + math.log(modelProb[uni_2][0])
			     	sentProb['UB']['-'] = sentProb['UB']['-'] + math.log(modelProb[uni_2][1])

			# Decision Making
			if(review[0] == '+'):
				if sentProb['UB']['+'] >= sentProb['UB']['-']:
					correct['UB'] = correct['UB'] + 1
				if sentProb['B']['+'] >= sentProb['B']['-']: 
					correct['B'] = correct['B'] + 1	
			else:
				if sentProb['UB']['-'] >= sentProb['UB']['+']:
					correct['UB'] = correct['UB'] + 1
				if sentProb['B']['-'] >= sentProb['B']['+']: 
					correct['B'] = correct['B'] + 1		
			 
		accuracy['UB'].append(correct['UB']*1.0/len(test_set))
		accuracy['B'].append(correct['B']*1.0/len(test_set))

	print accuracy['UB']
	print "Average Accuracy of the Unigram-Bigram model is " + str((sum(accuracy['UB'])/10)*100) + "%"	

	print accuracy['B']
	print "Average Accuracy of the Bigram model is " + str((sum(accuracy['B'])/10)*100) + "%"	

evaluation()


