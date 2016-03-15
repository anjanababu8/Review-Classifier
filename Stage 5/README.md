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
The code used for evaluation (<i>evaluation.py</i>) is included.<br/>
<b>Accuracy</b> of the model is <b>80%</b>

<i>NOTE: The code used in stage 4 (<b>unigram_model.py</b>) is included as a module in the evaluation.py to reuse the model training code.</i>
