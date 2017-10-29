##### DATA PREPROCESSING

#!/usr/bin/env python3
import json

#Open dataset and parses json and put entries in a nested list
with open('data/ent100k.json') as data_json:    
    data = json.load(data_json)

#Print total elements of the list
data_len = len(data)
print('There are {} total elements to analyze'.format(data_len+1))

#Take only elements that have a text field and put them in a new list
tex = []
for i in range(data_len):
    if 'text' in data[i]:
        tex.append(data[i]['text'])

#Print number of text elements of the list
tex_len = len(tex)
print('There are {} text elements to analyze'.format(tex_len+1))

#Remove newlines from text (swap them with spaces)
for i in range(tex_len):
        tex[i] = tex[i].replace('.\n','\n')
        tex[i] = tex[i].replace('\n','. ')

#Create a new txt file populated with text fields (one per line)
with open('data/text.txt','w') as text:
    for i in range(tex_len):
        text.write("%s\n\n" % tex[i])



