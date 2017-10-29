# nlp_fbtrex
Natural Language Processing for FbTrex. We use state-of-the-art NLP techniques to mine facebook users text from their post. 

1) Set up a python venv and install Stacy module (alpha)
```
$ python -m pip install -U venv
$ venv nlp
$ source nlp/bin/activate
$ pip install -U spacy
```
Later on we will also use gensim to provided training for our model 
2) Download dataset
```
$ wget -c http://facebook.tracking.exposed:XXXXX/
```
The dataset is a nested json, kindly provided by fbtrex team. At the moment this file is private, but you make your own using fbtrex tool!
Once downloaded put the file in the data directory and rename it ent100k.json (make is shorter for text, the processing is time consuming!) 
3) Run preprocessing.py
```
$ python preprocessing.py
```
This will parse the json and extract only the text fields. Any other relevant information (id, source etc.) is lost during this process. The parsed text is put in text.txt, with one review per line.
4) Apply Spacy NLP
Spacy makes it very simple to analyze text, since it uses only one function!
Run naive_nlp.py to process the text file in a basic way 
```
$ python naive_nlp.py
```
Now you can explore all the things that spacy does for you! Spacy provides non-destructive tokenization, named entity recognition, part-of-speech tagging, labelled dependency parsing, a built-in visualizer and much more!  

We will actually use Spacy's normalization pipeline to have the text ready for topic mining. Run nlp.py to have the text broken down into sentences and normalized: 
```
$ python nlp.py
```
For every step we take it's good to have a new file. After this snippet, you will find a new_text.txt in your data directory, make sure it contains the normalized text.
