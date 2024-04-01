import spacy
nlp = spacy.load('te_pipeline')
doc = nlp('నేను 27-09-2023 ఢిల్లీలో ఉన్నాను')
for ent in doc.ents:
    print(ent.text, ent.label_)
print(nlp.pipe_names)