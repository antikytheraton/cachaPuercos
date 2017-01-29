import csv
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
from sklearn import svm,metrics
from sklearn.cross_validation import train_test_split
import numpy as np
#from keras.utils import np_utils


with open('proces.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
def prepara_frase(data):
    features=[]
    feature={}
    targets=[]
    for i,vector in enumerate(data):
        if vector[0]!='-' and  vector[0]!='':
            feature['0']=str(data[i-2][1]).lower()
            feature['1']=str(data[i-1][1]).lower()
            feature['2']=str(data[i][1]).lower()
            feature['3']=str(data[i+1][1]).lower()
            feature['4']=str(data[i+2][1]).lower()
            features.append(feature)
            #print feature
            feature={}
            #if vector[0]!='af':
            targets.append(vector[0][0])
            #else:
                #targets.append('*')
    return features,targets

features,target=prepara_frase(data)
diccionario = dict((c, i) for i, c in enumerate(list(set(target))))
print(diccionario)

v = DictVectorizer(sparse=False)
v.fit(features)
joblib.dump(v, 'vectorizer.pkl')
transformed=v.transform(features)
print("Tenemos los vectores transformados")
print(transformed.shape)
#target to one hot for lstm model
#y = np.zeros((len(target), len(diccionario)), dtype=np.bool)
"""for index,tar in enumerate(target):
    print("antes de categorizar: "+str(tar))
    print(diccionario[tar])
    y[index,diccionario[tar]]=1
    print("despues de categorizar: "+str(y[index]))
raw_input()"""
#X = np.zeros((max_sequence, vec.shape[1], dtype=np.bool)
"""    for i,word in enumerate(vec):
        X_[i]=word
    return X_
"""


# define the LSTM model
def createModel(X,y):
    model = Sequential()
    model.add(LSTM(256, input_shape=(X.shape[1])))
    model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model


X_train, X_test, y_train, y_test=train_test_split(transformed,target,test_size=0.2,random_state=42)
#print(X_train[0])
#print(len(X_train))
clf = svm.SVC(C=1,kernel='linear')
clf.fit(X_train, y_train)
acc=metrics.accuracy_score(y_test,clf.predict(X_test))
joblib.dump(clf, 'clasifier.pkl')
print(acc)
