# Tokenisasi dan Pranata Kalimat
import nltk
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from transformers import pipeline
from gensim.summarization import summarize

nltk.download('punkt')

# Tokenisasi dengan NLTK
sentences = nltk.sent_tokenize(text)

# Ekstraksi Fitur dengan SpaCy
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)

# Ringkasan Ekstraktif dengan Sumy
parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LsaSummarizer()
summary_sumy = summarizer(parser.document, 5)  # Ringkasan dengan 5 kalimat

# Ringkasan Ekstraktif dengan Gensim
summary_gensim = summarize(text, word_count=100)

# Ringkasan Abstraktif dengan BERT
summarizer_bert = pipeline("summarization")
summary_bert = summarizer_bert(text, max_length=150, min_length=50, do_sample=False)

# Menampilkan hasil ringkasan
print("Ringkasan dengan Sumy:")
for sentence in summary_sumy:
    print(sentence)

print("\nRingkasan dengan Gensim:")
print(summary_gensim)

print("\nRingkasan dengan BERT:")
print(summary_bert[0]['summary_text'])
