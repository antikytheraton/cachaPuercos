from sklearn.externals import joblib
import os

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
    hash_path = os.path.realpath("hasher_cache/vectorizer.pkl")
    clf_path = os.path.realpath("clf_cache/clasifier.pkl")
    clf = joblib.load(clf_path)
    vectorizer=joblib.load(hash_path)
    lista=frase2lista(frase)
    features=prepara_frase(lista)
    features=vectorizer.transform(features)
    clases=clf.predict(features)
    return lista,clases
