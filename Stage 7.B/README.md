# Review-Classifier
<b>Step 7.B : Evaluating the Model (10-fold cross validation)</b>
<ul>
<li>Divided the data set into 10 equal parts(each containing 60 reviews and approximately same no. of + and - samples).</li>
<li>Trained with 9 parts and tested on the left out 1 part.</li>
<li>Log probabilities (used <b>math</b> library) are used for finding the membership probabilities to prevent underflow.</li>
<li>Accuracy (correctPredictions/numberOfReviews) for each round is also calculated.</li>
<li>Repeated the process 10 times.</li>
<li>Calculated the average accuracy.</li>
</ul>
The code used for evaluation (<b><i>evaluation.py</i></b>) is included.<br/>
 
<i>NOTE: The code used for creating the model (uni_bi_model.py) is included as a module in the evaluation.py to reuse the model training code. Reviews in cleaned_data.txt is ordered - + - + - ... to ensure approximately equal number of + and - reviews are held out. </i>
