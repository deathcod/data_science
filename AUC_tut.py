import pandas as pd
#import urllib
#url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data'
#file('data/diabetes.csv','w').write(urllib.urlopen(url).read())
col_names = ['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
pima = pd.read_csv('data/diabetes.csv',header = None ,names = col_names)

#print pima.head()

feature_cols = ['pregnant','insulin','bmi','age']
x = pima[feature_cols]
y = pima.label

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x,y)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train,y_train)


y_class_pred = logreg.predict(X_test)

from sklearn import metrics

#print metrics.accuracy_score(y_test,y_class_pred)
#print y_test.value_counts()

confusion = metrics.confusion_matrix(y_test,y_class_pred)

TP = confusion[1,1]
TN = confusion[0,0]
FP = confusion[0,1]
FN = confusion[1,0]


#____________CLASSIFICATION ACCURACY_____________
print ((TP + TN) / float(TP + TN + FP + FN))
print metrics.accuracy_score(y_test,y_class_pred)
#the above you print is the classification accuracy
#it suggests overall how often the classifier is correct.

#_____________CLASSIFICATION ERROR_______________
print ((FP + FN) / float(TP + TN + FP +FN))
print 1 - metrics.accuracy_score(y_test,y_class_pred) 
# How often the classifier is wrong

#______________SENSITIVITY :: RECALL_______________________
print TP / float(TP + FN)
print metrics.recall_score(y_test,y_class_pred)

#______________FALSE POSITIVE RATE_________________________
print (FP / float(TN + FP))


#______________PRECISION___________________________________
print TP / float(TP + FP)
print metrics.precision_score(y_test,y_class_pred)
#how precisily the classifier is classifing the positive instances





#print X_test[y_class_pred<y_test]
#FN :: print X_test[y_test<y_class_pred]