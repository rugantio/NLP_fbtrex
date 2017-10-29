##### TOKENIZATION for phrase modeling

#Define some functions to have a tidy test
def punct_space(token):
    """
    helper function to eliminate tokens
    that are pure punctuation or whitespace
    """
    return token.is_punct or token.is_space

def line_review(filename):
    """
    generator function to read in reviews from the file
    and un-escape the original line breaks in the text
    """
    
    with open(filename) as f:
        for review in f:
            yield review.replace('\\n', '\n')
            
def lemmatized_sentence_corpus(filename):
    """
    generator function to use spaCy to parse reviews,
    lemmatize the text, and yield sentences
    """
    for parsed_review in nlp.pipe(line_review(filename),batch_size=10000, n_threads=4):
        for sent in parsed_review.sents:
            yield u' '.join([token.lemma_ for token in sent if not punct_space(token)])

#Create a new file with a clean text (without punctuation or caps)
with open('data/new_text.txt', 'w') as f:
    for sentence in lemmatized_sentence_corpus('data/text2.txt'):
        f.write(sentence + '\n')
