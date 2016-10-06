from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk import word_tokenize as wn
import nltk

def freq_dis(text):
	x=wn(text)
	x_len = len(x)
	x_new = set(x)
	x_list = [i for i in x_new if ((x.count(i)*100)/x_len)<=20]
	return x_list
	pass	


x = input()
A = []
for i in range(x):
	text = raw_input()
	A.append(text)
	pass

raw_input()
B = []
for i in range(x):
	text = raw_input()
	t = freq_dis(text)
	#print t
	B.append(' '.join(t))
	pass

vect = CountVectorizer()

X_train = vect.fit_transform(B)
y_train = range(x+1)[1:]


X_test = vect.transform(A)

nb = MultinomialNB()
nb.fit(X_train,y_train)
y_test = nb.predict(X_test)

for i in y_test:
	print i
