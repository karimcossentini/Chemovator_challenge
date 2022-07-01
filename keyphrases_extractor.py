from keybert import KeyBERT
from keyphrase_vectorizers import KeyphraseCountVectorizer
from flair.embeddings import TransformerDocumentEmbeddings
from bs4 import BeautifulSoup
import re
import os
import nltk
nltk.download('words')

def scored_keyphrases_extractor(keyphrases):
    """
    extract the keyphrases from a list of scored keyphrases
    Arguments: keyphrases (list)
    Returns: list of keyphrases (list)
    """
    results = []
    for scored_keyphrases in keyphrases:
        for keyword in scored_keyphrases:
            if isinstance(keyword, str):
                results.append(keyword)
    return results


words = set(nltk.corpus.words.words())


def remove_meaningful_words(text):
    """
    filter out meaningful words from the text
    Arguments: text (str)
    Returns: clean text (str)
    """
    return " ".join(w for w in nltk.wordpunct_tokenize(text) if w.lower() in words or not w.isalpha())

def clean_text(text):

    text = ' '.join(text)
    text = re.sub('\n+', ' ', str(text))
    text = re.sub(' +', ' ', str(text))
    return text

def extract_text_xml(path,file):
    with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
        data = f.read()
    soup = BeautifulSoup(data, features="xml")
    pageText = soup.findAll(text=True)
    return pageText

def keybert_extractor(file_tag):
    if file_tag == 'AT':
        vectorizer = KeyphraseCountVectorizer(spacy_pipeline='de_core_news_sm', pos_pattern='<ADJ.*>*<N.*>+',
                                              stop_words='german')
        bert = KeyBERT(model=TransformerDocumentEmbeddings('dbmdz/bert-base-german-uncased'))
        return bert, vectorizer
    else:
        bert = KeyBERT()
    return bert, None

