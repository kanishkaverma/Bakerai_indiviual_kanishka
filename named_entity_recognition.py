import nltk
import spacy

ex = "I live in India. How do i get to the shop? "
model = 'en_core_web_sm'
nlp = spacy.load('en_core_web_sm')
 
 
def convert_input_ner(user_input): 
    for tup in ner(user_input): 
        # print(tup)
        if tup[1] == 'GPE': 
           return [replace_in_text(tup[0],tup[1],user_input),tup[0]]
    return [user_input, ""]

def ner(user_input): 
    nlpi = spacy.load('en_core_web_sm')
    doc = nlpi(user_input)
    # print(doc.ents)
    return [(X.text, X.label_) for X in doc.ents]


def preprocess_ner(sentence):
    sentence = nltk.word_tokenize(sentence )
    sentence =  nltk.pos_tag(sentence)
    
    return sentence 


def main(): 
 
    print(convert_input_ner("I live in Canada"))
     
    print(convert_input_ner("show me London on a map"))

def process_after_ner(text, replaced_word): 

    return text.replace("<GPE>", replaced_word)

def replace_in_text(text, label, input_text): 
    return input_text.replace(text, f'<{label}>')
