# OFTEN NATURAL LANGUAGE PROCESSING IS DONE WITH WORD COUNTS: CREATE A VECTOR OF ALL POSSIBLE WORDS AND PUT THE OCCURANCES IN A VECTOR
# AFTERWARDS, TAKE THE INNER PRODUCT ("COSINE SIMILARITY" [A*B/(|A|*|B|)]) TO SEE HOW THE TEXTS COMPARE

# TERM FREQUENCY = IMPORTANCE OF TERM WITHIN DOCUMENT; TF(D, T) = NUMBER OF OCCURANCES TERM T IN DOCUMENT D
# INVERSE DOCUMENT FREQUENCY = IMPORTANCE OF TERM WITHIN MULTIPLE DOCUMENTS; 
#     IDF(M_T) = LOG(N/M_T), N IS NUMBER OF DOCUMENTS, M NUMBER OF DOCUMENTS WITH THAT TERM
# FORMULA: W(X,Y) = TF(Y, X)*IDF(M_X)

import numpy
import pandas
import matplotlib
from matplotlib import pyplot
import seaborn
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

import sklearn
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline

messages = [line.rstrip() for line in open('smsspamcollection/SMSSpamCollection')]
print(len(messages))

messages = pandas.read_csv('smsspamcollection/SMSSpamCollection', sep = '\t', names = ['label', 'message'])
messages.info()
messages['length of message'] = messages['message'].apply(len)
print(messages.groupby('label')['length of message'].mean())

seaborn.FacetGrid(messages, hue = "label", size = 6, aspect = 2, palette = 'coolwarm', legend_out = True).map(\
seaborn.distplot,'length of message', kde = False, bins = 100)
pyplot.show()

# FILTER OUT PUNCTUATION:
def durk(x):
    a = []
    for element in x:
        if element in string.punctuation:
            a.append('')
        else:
            a.append(element)
    return ''.join(a)

# FILTER OUT STOPWORDS (E.G.: "DON'T"):
def durk_two(x):
    a = x.split()
    b = []
    for element in a:
        if element.lower() not in stopwords.words('english'):
        #     b.append('')
        # else:
            b.append(element)
    return ' '.join(b)
        
messages['message'] = messages['message'].apply(durk_two).apply(durk).apply(durk_two)

# CREATE INSTANCE OF COUNTVECTORIZER:
bag_of_words = CountVectorizer(analyzer = 'word')
# USE TERMS IN THIS FILE/DATAFRAME:
bag_of_words.fit(messages['message'])
print(len(bag_of_words.vocabulary_))
# MAKE A SPARSE WORD-COUNTING MATRIX OUT OF THIS:
message_matrix = bag_of_words.transform(messages['message'])
print(message_matrix.shape)

# MAKE TFIDF OF EVERY ELEMENT IN THE MATRIX:
tfidf = TfidfTransformer()
tfidf.fit(message_matrix)
message_tfidf = tfidf.transform(message_matrix)
print(message_tfidf[0])

# USING MILTINOMIAL NAIVE BAYES AS A FIT HERE:
spam_detection = MultinomialNB()
spam_detection.fit(message_tfidf, messages['label'])
spam_prediction = spam_detection.predict(message_tfidf)

print("RATIO OF CORRECTLY PREDICTED AS SPAM OVER TOTAL NUMBER OF MESSAGES: ", numpy.sum(numpy.equal(spam_prediction, messages['label']))/len(messages['label']))

Xtr, Xts, ytr, yts = train_test_split(messages['message'], messages['label'], test_size = 0.33)

pipeline = Pipeline([
    ("bag_of_words", CountVectorizer(analyzer = 'word')),
    ("tfidf", TfidfTransformer()),
    ("classifier", MultinomialNB())
])

pipeline.fit(Xtr,ytr)
pred = pipeline.predict(Xts)

print(classification_report(yts, pred))
print(confusion_matrix(yts,pred))