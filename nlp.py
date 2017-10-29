##### TOKENIZATION for phrase modeling
import spacy

#Import Spacy Spanish lang model
nlp = spacy.load('es_core_web_sm')

#Eliminate tokens that are pure punctuation or whitespace
def punct_space(token):
    """
    helper function to 
    """
    return token.is_punct or token.is_space

#Read in reviews from the file and un-escape the original line breaks in the text
def line_review(filename):
     with open(filename) as f:
        for review in f:
            yield review.replace('\\n', '\n')
            
#Use spaCy to parse reviews, lemmatize the text, and yield sentences
def lemmatized_sentence_corpus(filename):
   for parsed_review in nlp.pipe(line_review(filename),batch_size=100, n_threads=4):
        for sent in parsed_review.sents:
            yield u' '.join([token.lemma_ for token in sent if not punct_space(token)])

#Create a new file with a clean text (without punctuation or caps)
with open('../nlp/data/new_text.txt', 'w') as f:
    for sentence in lemmatized_sentence_corpus('../nlp/data/text.txt'):
        f.write(sentence + '\n')
