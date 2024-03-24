# OFTEN NATURAL LANGUAGE PROCESSING IS DONE WITH WORD COUNTS: CREATE A VECTOR OF ALL POSSIBLE WORDS AND PUT THE OCCURANCES IN A VECTOR
# AFTERWARDS, TAKE THE INNER PRODUCT ("COSINE SIMILARITY" [A*B/(|A|*|B|)]) TO SEE HOW THE TEXTS COMPARE ON THE BASIS OF THEIR VECTORS

# TERM FREQUENCY = IMPORTANCE OF TERM WITHIN DOCUMENT; TF(D, T) = NUMBER OF OCCURANCES TERM T IN DOCUMENT D
# INVERSE DOCUMENT FREQUENCY = IMPORTANCE OF TERM WITHIN MULTIPLE DOCUMENTS; 
#     IDF(M_T) = LOG(N/M_T), N IS NUMBER OF DOCUMENTS, M NUMBER OF DOCUMENTS WITH THAT TERM
# FORMULA: TF-IDF = W(X,Y) = TF(Y, X)*IDF(M_X)

import numpy
import pandas
from matplotlib import pyplot
import seaborn
#  DOWNLOAD IS NECESSARY THE VERY FIRST TIME
#  import nltk
#  nltk.download('stopwords')
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline


################################################################################
#  PREPROCESSING
################################################################################

messages = pandas.read_csv('SMSSpamCollection', sep = '\t', names = ['label', 'message'])
messages.info()
print( '\n\n' )

messages['length of message'] = messages['message'].apply(len)
print( 'AVERAGE LENGTH OF THE MESSAGES:\n', messages.groupby('label')['length of message'].mean())
print( '\n\n' )

#  OOP-WAY OF CREATING THE FIGURE:
canvas = pyplot.figure( figsize = ( 15, 6 ) )
#  CREATES AXES AS PERCENTAGE OF RANGE OF X AND Y (XMIN, YMIN, X-SCALE, Y-SCALE)
axes = canvas.add_axes([ .15, .15, .8, .8 ])
seaborn.histplot( x = 'length of message', hue = 'label', data = messages, palette = 'plasma', kde = False, bins = 100, ax = axes )
axes = pyplot.gca()
axes.set_xlim([0,1000])
axes.set_ylim([0,1e3])
#  NOTE, THIS IS DIFFERENT FROM FUNCTIONAL FORM ABOVE
axes.set_xlabel("Number of characters")
axes.set_ylabel("Count")
axes.set_title("NUMBER OF MESSAGES WITH GIVEN LENGTH")
#  FUNCTIONAL-WAY:
#  seaborn.FacetGrid(messages, hue = "label", height = 6, aspect = 2, palette = 'coolwarm', legend_out = True).map( seaborn.histplot,'length of message', kde = False, bins = 100 )
pyplot.show()
print( '\n\n' )

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
            b.append(element)
    return ' '.join(b)
        
messages['message'] = messages['message'].apply(durk_two).apply(durk).apply(durk_two)

################################################################################
#  ANALYSIS
################################################################################

# CREATE INSTANCE OF COUNTVECTORIZER:
bag_of_words = CountVectorizer(analyzer = 'word')
# USE TERMS IN THIS FILE/DATAFRAME:
bag_of_words.fit(messages['message'])
print( 'THE NUMBER OF RELEVANT, DIFFERENT WORDS IN THE DATA SET: ', len(bag_of_words.vocabulary_))
print( '\n\n' )
# MAKE A SPARSE WORD-COUNTING MATRIX OUT OF THIS:
message_matrix = bag_of_words.transform(messages['message'])
print( 'THE MESSAGES PUT INTO THE BAG OF WORDS, THE CREATE A MATRIX OF SHAPE: ', message_matrix.shape)
print( '\n\n' )

# MAKE TFIDF OF EVERY ELEMENT IN THE MATRIX:
tfidf = TfidfTransformer()
tfidf.fit(message_matrix)
message_tfidf = tfidf.transform(message_matrix)
print( 'TFIDF-SCORE FOR THE FIRST MESSAGE:\n', message_tfidf[0])
print( '\n\n' )

# USING MILTINOMIAL NAIVE BAYES AS A FIT HERE:
spam_detection = MultinomialNB()
spam_detection.fit(message_tfidf, messages['label'])
spam_prediction = spam_detection.predict(message_tfidf)

print( 'RESULTS FOR MANUAL PROCESS:\n' )
print("RATIO OF CORRECTLY PREDICTED AS SPAM OVER TOTAL NUMBER OF MESSAGES: ", numpy.mean( spam_prediction == messages[ 'label' ] ) )
print( '\n\n' )

#  NOTE THAT THE WHOLE PREVIOUS PROCESS CAN ALSO BE DONE AUTOMATICALLY USING A PIPELINE
Xtr, Xts, ytr, yts = train_test_split(messages['message'], messages['label'], test_size = 0.33)

pipeline = Pipeline([
    ("bag_of_words", CountVectorizer(analyzer = 'word')),
    ("tfidf", TfidfTransformer()),
    ("classifier", MultinomialNB())
])

pipeline.fit(Xtr,ytr)
pred = pipeline.predict(Xts)

print( 'RESULTS FOR PIPELINE:\n' )
print(classification_report(yts, pred))
print(confusion_matrix(yts,pred))
