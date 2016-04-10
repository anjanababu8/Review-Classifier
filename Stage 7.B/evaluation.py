import pickle
import math
import uni_bi_model  # Module made in Step 4 included to make the model

# Counts the number of +/- ve reviews in the corpus 	
def countReviews(corpus,sign):
	count = 0
	for review in corpus:
		words = review.split()
		if(words[0] == sign):
			count = count + 1
	return count	

def evaluation():
	accuracy = []
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
		
		modelProbabilities = uni_bi_model.trainingTheModel(training_set)

		correct = 0
		countOfReviews  = [countReviews(training_set, '+'), countReviews(training_set, '-')] 
		for review in test_set:
			posProb = math.log(1.0*countOfReviews[0]/len(training_set))
			negProb = math.log(1.0*countOfReviews[1]/len(training_set))
			probability = [posProb, negProb]  
				
			words = review.split()
			if(len(words)<2):
				continue		
		        for i in range(0,len(words)-1):
		           word = words[i] + ' ' + words[i+1]
			   if i == 0: #P(START word | ---)
			     probability[0] = probability[0] + math.log(modelProbabilities['START '+ words[1]][0])
			     probability[1] = probability[1] + math.log(modelProbabilities['START '+ words[1]][1]) 	
			   elif word in modelProbabilities:
			     probability[0] = probability[0] + math.log(modelProbabilities[word][0])
			     probability[1] = probability[1] + math.log(modelProbabilities[word][1]) 
			   else: # Bigram not in vocabulary as its count<2 then consider its unigram probability
			     probability[0] = probability[0] + math.log(modelProbabilities[words[i]][0])
			     probability[0] = probability[0] + math.log(modelProbabilities[words[i+1]][0])
			     probability[1] = probability[1] + math.log(modelProbabilities[words[i]][1])
			     probability[1] = probability[1] + math.log(modelProbabilities[words[i+1]][1])
			# P(word STOP ...)
			probability[0] = probability[0] + math.log(modelProbabilities[words[len(words)-1]+' STOP'][0])
			probability[1] = probability[1] + math.log(modelProbabilities[words[len(words)-1]+' STOP'][1]) 	
			
			if((probability[0]>=probability[1] and words[0] == '+') or 
			   (probability[1]>=probability[0] and words[0] == '-')):
				correct = correct + 1
		accuracy.append(correct*1.0/len(test_set))
		print accuracy
	print "Accuracy of the model is " + str((sum(accuracy)/10)*100) + "%"	

evaluation()


