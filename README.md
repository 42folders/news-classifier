# An NLP learning journey

Documenting my foray into Natural Language Processing with Python here -- training of text classifiers for classification of the Huffington Post news dataset. 

This dataset has more than 200K records -- lack of training examples is not a limiting factor. Even for the smallest categories, there are at least 1000 samples. However this is an extremely imbalanced dataset, which gives opportunities to practise techniques to correct for the imbalance. 

Done: 

1. Initial screen of 4 conventional classification algorithms (Naive Bayes classifier, Random Forest, Logistic Regression and Linear Support Vector classifier)
   - LinearSVC did the best (followed closely by Logistic Regression)
2. Further hyperparameter optimisation of LinearSVC model (average weighted F1 score = 76%)

In progress: 

3. Training a transformer model (DistilBERT) using the HuggingFace Trainer class to see how its performance compares with the non-transformer model. 
 
