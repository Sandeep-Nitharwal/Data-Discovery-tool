import spacy

nlp = spacy.load('en_core_web_sm')

def detect_pii_nlp(data):
    doc = nlp(data)
    detected_pii = []
    for entity in doc.ents:
        if entity.label_ in ['PERSON', 'GPE', 'ORG']:
            detected_pii.append((entity.text, entity.label_))
    return detected_pii
