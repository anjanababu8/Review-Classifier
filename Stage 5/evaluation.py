import pickle
import math
import unigram_model  # Module made in Step 4 included to make the model

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
		training_set = list(set(corpus) - set(test_set))
		
		modelProbabilities = unigram_model.step4(training_set)

		correct = 0
		countOfReviews  = [countReviews(training_set, '+'), countReviews(training_set, '-')] 
		for review in test_set:
			posProb = math.log(1.0*countOfReviews[0]/len(training_set))
			negProb = math.log(1.0*countOfReviews[0]/len(training_set))
			probability = [posProb, negProb]  

			words = review.split()
			for word in words[1:]:
				probability[0] = probability[0] + math.log(modelProbabilities[word][0])
				probability[1] = probability[1] + math.log(modelProbabilities[word][1]) 
			if((probability[0]>=probability[1] and words[0] == '+') or (probability[1]>=probability[0] and words[0] == '-')):
				correct = correct + 1
		accuracy.append(correct*1.0/len(test_set))
	print "Accuracy of the model is " + str((sum(accuracy)/10)*100) + "%"	

evaluation()


