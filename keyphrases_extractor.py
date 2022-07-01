from keybert import KeyBERT
from keyphrase_vectorizers import KeyphraseCountVectorizer
from flair.embeddings import TransformerDocumentEmbeddings
from bs4 import BeautifulSoup
import re
import os
import nltk
from googletrans import Translator

nltk.download('words')
words = set(nltk.corpus.words.words())


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




def remove_meaningful_words(text):
    """
    filter out meaningful words from the text
    Arguments: text (str)
    Returns: clean text (str)
    """
    return " ".join(w for w in nltk.wordpunct_tokenize(text) if w.lower() in words or not w.isalpha())

def clean_text(text):
    """
    clean text
    Arguments: text (str)
    Returns: cleaned text (str)
    """
    text = ' '.join(text)
    text = re.sub('\n+', ' ', str(text))
    text = re.sub(' +', ' ', str(text))
    return text

def extract_text_xml(path,file):
    """
    extract abstract text from xml file
    Arguments: path (str)
    Arguments: file (str)
    Returns: extracted text (str)
    """
    pageText=[]
    with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
        data = f.read()
    soup = BeautifulSoup(data, features="xml")
    #pageText = soup.findAll(text=True)
    for line in soup.find_all('abstract'):
        pageText.append(line.text)
    return pageText

def keybert_extractor(lang):
    """
    initialize bert model and vectorizer
    Arguments: lang (str)
    Returns: keybert model and vectorizer
    """
    if lang != 'en':
        vectorizer = KeyphraseCountVectorizer(spacy_pipeline='de_core_news_sm', pos_pattern='<ADJ.*>*<N.*>+',
                                              stop_words='german')
        bert = KeyBERT(model=TransformerDocumentEmbeddings('dbmdz/bert-base-german-uncased'))
        return bert, vectorizer
    else:
        bert = KeyBERT()
    return bert, None


def detect_lang(text):
    """
    detect the language of text data
    Arguments: text (str)
    Returns: detected language (str)
    """
    translator = Translator()
    return translator.detect(str(text)).lang