import spacy
# import en_core_web_sm

nlp = spacy.load('en_core_web_sm')
# nlp = en_core_web_sm.load()



# Function to process text using NLP
def process_text(text):
    doc = nlp(text)
    processed_text = ' '.join([token.lemma_ for token in doc if not token.is_stop])
    return processed_text


