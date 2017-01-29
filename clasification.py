from sklearn.externals import joblib
import numpy as np
def frase2lista(frase):
    return ['-','-']+frase.split(" ")+['-','-']
def prepara_frase(data):
    features=[]
    feature={}
    for i,vector in enumerate(data):
        if vector[0]!='-' and  vector[0]!='':
            print data[i]
            feature['0']=str(data[i-2]).lower()
            feature['1']=str(data[i-1]).lower()
            feature['2']=str(data[i]).lower()
            feature['3']=str(data[i+1]).lower()
            feature['4']=str(data[i+2]).lower()
            features.append(feature)
            feature={}
    return features
def getNer(frase):
    lista=frase2lista(frase)
    features=prepara_frase(lista)
    vectorizer=joblib.load("vectorizer.pkl")
    features=vectorizer.transform(features)
    clf=joblib.load("clasifier.pkl")
    clases=clf.predict(features)
    return lista,clases
