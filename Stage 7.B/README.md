# Review-Classifier
<b>Step 7.B : Evaluating the Model(Uni-Bi) (10-fold cross validation)</b>
<ul>
<li>Divided the data set into 10 equal parts(each containing 60 reviews and approximately same no. of + and - samples).</li>
<li>Trained with 9 parts and tested on the left out 1 part.</li>
<li>Log probabilities (used <b>math</b> library) are used for finding the membership probabilities to prevent underflow.</li>
<li>Accuracy (correctPredictions/numberOfReviews) for each round is also calculated.</li>
<li>Repeated the process 10 times.</li>
<li>Calculated the average accuracy.</li>
</ul>
The code used for evaluation (<b><i>evaluation.py</i></b>) is included.<br/>
<i>NOTE: The code used for creating the model (uni_bi_model.py) is included as a module in the evaluation.py to reuse the model training code. Reviews in cleaned_data.txt is ordered - + - + - ... to ensure equal number of + and - reviews are held out. </i><br/>

<b>How Bag Of Words counts were calculated?</b><br/>
If a bigram in the training set is present in the vocabulary then the corresponding unigram count is reduced by the bigram count. In doing so, a unigram which became part of two bigram(eg. "not" in "book not good") gets its count decremented twice and results in a negative count. This case is dealt by making those unigram counts whose count became negative to 0.

<b>(UB)</b> The Unigram-Bigram Naive Bayes model was evaluated considering both the bigram features and the unigram features. That is, if a bigram in the review is not present in the vocabulary(as its count &lt; 2) then we considered the corresponding unigram probabilities.<br><br/>
Average <b>Accuracy</b> of the Unigram-Bigram model is <b>83.8333333333%</b><br/>
<p>Accuracies of the model in each iteration:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	1<sup>st</sup> : 81.66666666666667%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	2<sup>nd</sup> : 78.33333333333333%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	3<sup>rd</sup> : 81.66666666666667%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	4<sup>th</sup> : 85%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	5<sup>th</sup> : 81.66666666666667%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	6<sup>th</sup> : 76.66666666666667%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	7<sup>th</sup> : 88.33333333333333%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	8<sup>th</sup> : 85%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	9<sup>th</sup> : 95%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	10<sup>th</sup> : 85%

<hr>
<b>(B)</b> We have also evaluated the model by considering only bigram features. That is, if a bigram in the review is not present in the vocabulary(as its count &lt; 2) then we didn't consider the corresponding unigram probabilities, instead just did smoothing.<br/><br/> 
Average <b>Accuracy</b> of the Bigram model is <b>70.5%</b><br/>
<p>Accuracies of the model in each iteration:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	1<sup>st</sup> : 65%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	2<sup>nd</sup> : 63.33333333333333%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	3<sup>rd</sup> : 56.66666666666667%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	4<sup>th</sup> : 73.33333333333333%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	5<sup>th</sup> : 80%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	6<sup>th</sup> : 66.666666666667%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	7<sup>th</sup> : 71.66666666666667%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	8<sup>th</sup> : 68.33333333333333%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	9<sup>th</sup> : 81.66666666666667%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	10<sup>th</sup> : 78.33333333333333%

