
##### LANGUAGE PROCESSING
import spacy

#Open text file and store content in a single str
with open('data/text2.txt','r') as text:
    full_txt = text.read()

#Import Spact spanish lang model
nlp = spacy.load('es_core_web_sm')

#Initialize Spacy pipeline (tokenize, parse and tag the full text)
# WARNING: Resource consuming!
doc = nlp(full_txt)

##### VISUALIZATION
from spacy import displacy
options = {'compact': False, 'bg': 'ffffff',
           'color': 'black', 'font': 'Arial', 'distance':600}
#Displacy provides arch visualization via web server
displacy.serve(doc, style='dep', options=options)
#Show text with highlighted entities
#displacy.serve(doc, style='ent', options=options)
