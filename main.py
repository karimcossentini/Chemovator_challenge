import os
import re
from keyphrases_extractor import keybert_extractor, clean_text, scored_keyphrases_extractor, remove_meaningful_words, \
    extract_text_xml, detect_lang
import models
from database import engine,SessionLocal

models.Base.metadata.create_all(engine)
db = SessionLocal()

for folders in os.listdir('data'):
    path = os.path.join('data', folders)

    for file in os.listdir(path):
        if file[-4:] == '.xml':

            pageText = extract_text_xml(path, file)

            print(file)

            if pageText:
                language = detect_lang(' '.join(pageText))
                bert, vectorizer = keybert_extractor(language)
                pageText = clean_text(pageText)

                if language != 'en':
                    keywords = bert.extract_keywords(pageText, vectorizer=vectorizer)
                    keywords = scored_keyphrases_extractor(keywords)
                else:
                    pageText = re.sub(r'\w*\d\w*', '', str(pageText))
                    pageText = remove_meaningful_words(pageText)
                    keywords = bert.extract_keywords(pageText, keyphrase_ngram_range=(1, 3), stop_words="english", top_n=5)
                    keywords = scored_keyphrases_extractor(keywords)
            else:
                keywords = 'abstract not found'

            doc = models.DocInfo(file_name=file, keyphrases=keywords)
            db.add(doc)
            db.commit()
            db.refresh(doc)


