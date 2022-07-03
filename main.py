import os
import re
from keyphrases_extractor import keybert_extractor, clean_text, scored_keyphrases_extractor, remove_meaningful_words, \
    extract_text_xml, detect_lang
import models
from database import engine, SessionLocal
import logging

# implement an event logging system
logging.basicConfig(filename='patent_doc_database.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()

# Start database session
models.Base.metadata.create_all(engine)
db = SessionLocal()

# loop through data samples
for folders in os.listdir('data'):
    path = os.path.join('data', folders)

    for file in os.listdir(path):
        if file[-4:] == '.xml':

            # Extract text (abstract) from xml files
            pageText = extract_text_xml(path, file)

            if pageText:
                # Detect text language to determine which BERT model to use
                language = detect_lang(' '.join(pageText))
                # initialize bert model and vectorizer that calculates the document-keyphrase matrices.
                bert, vectorizer = keybert_extractor(language)
                # Clean text
                pageText = clean_text(pageText)

                if language != 'en':
                    # extract keyphrases
                    keywords = bert.extract_keywords(pageText, vectorizer=vectorizer)
                    keywords = scored_keyphrases_extractor(keywords)
                else:
                    pageText = re.sub(r'\w*\d\w*', '', str(pageText))
                    pageText = remove_meaningful_words(pageText)
                    # extract keyphrases
                    keywords = bert.extract_keywords(pageText, keyphrase_ngram_range=(1, 3), stop_words="english",
                                                     top_n=5)
                    keywords = scored_keyphrases_extractor(keywords)
            else:
                keywords = 'abstract not found'

            # Insert data into the table
            doc = models.DocInfo(file_name=file, keyphrases=keywords)
            db.add(doc)
            db.commit()
            db.refresh(doc)
            logger.info('data inserted successfully %s: ', file)
