# Review-Classifier
<b>Step 5 : Evaluating the Model (10-fold cross validation)</b>
<ul>
<li>Divided the data set into 10 equal parts(each containing 60 reviews and approximately same no. of + and - samples).</li>
<li>Trained with 9 parts and tested on the left out 1 part.</li>
<li>Log probabilities (used <b>math</b> library) are used for finding the membership probabilities to prevent underflow.</li>
<li>Accuracy (correctPredictions/numberOfReviews) for each round is also calculated.</li>
<li>Repeated the process 10 times.</li>
<li>Calculated the average accuracy.</li>
</ul>
The code used for evaluation (<b><i>evaluation.py</i></b>) is included.<br/>
Average <b>Accuracy</b> of the model is <b>82.3333333333%</b><br/>
<p>Accuracies of the model in each iteration:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	1<sup>st</sup> : 78.33333333333333%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	2<sup>nd</sup> : 73.33333333333333%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	3<sup>rd</sup> : 68.33333333333333%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	4<sup>th</sup> : 85%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	5<sup>th</sup> : 78.33333333333333%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	6<sup>th</sup> : 85%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	7<sup>th</sup> : 86.66666666666667%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	8<sup>th</sup> : 85%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	9<sup>th</sup> : 93.33333333333333%<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	10<sup>th</sup> : 90%
</p>

 
<i>NOTE: The code used in stage 4 (unigram_model.py) is included as a module in the evaluation.py to reuse the model training code. Reviews in cleaned_data.txt is ordered - + - + - ... to ensure approximately equal number of + and - reviews are held out. (Model exporting code is given in Stage 4)</i>

