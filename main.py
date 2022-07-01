import os
import re
from keyphrases_extractor import keybert_extractor, clean_text, scored_keyphrases_extractor, remove_meaningful_words, \
    extract_text_xml

for folders in os.listdir('data'):
    path = os.path.join('data', folders)

    bert, vectorizer = keybert_extractor(os.listdir(path)[0][:2])
    for file in os.listdir(path)[:5]:
        if file[-4:] == '.xml':

            pageText = extract_text_xml(path, file)

            print(file)

            pageText = clean_text(pageText)

            if file[:2] == 'AT':
                keywords = bert.extract_keywords(pageText, vectorizer=vectorizer)
                keywords = scored_keyphrases_extractor(keywords)
            else:
                pageText = re.sub(r'\w*\d\w*', '', str(pageText))
                pageText = remove_meaningful_words(pageText)
                keywords = bert.extract_keywords(pageText, keyphrase_ngram_range=(1, 3), stop_words="english", top_n=5)
                keywords = scored_keyphrases_extractor(keywords)

            print(keywords)
            print('____________________________________________________________')
