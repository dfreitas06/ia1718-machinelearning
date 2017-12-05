import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

vowels =     ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
consonants = ('b', 'B', 'c', 'C', 'd', 'D', 'f', 'F', 'g', 'G',
              'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M',
              'n', 'N', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S',
              't', 'T', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y',
              'z', 'Z')
accents =    ('á', 'Á', 'â', 'Â', 'à', 'À', 'ã', 'Ã', 'é', 'É',
              'ê', 'Ê', 'è', 'È', 'í', 'Í', 'î', 'Î', 'ì', 'Ì',
              'ó', 'Ó', 'ô', 'Ô', 'ò', 'Ò', 'õ', 'Õ', 'ú', 'Ú',
              'û', 'Û', 'ù', 'Ù')
a_variants =         ('a', 'A', 'á', 'Á', 'â', 'Â', 'à', 'À', 'ã', 'Ã')

def countVowels(str):
    count = 0
    for c in str:
        if c in vowels:
            count += 1
    return count

def countConsonants(str):
    count = 0
    for c in str:
        if c in consonants:
            count += 1
    return count

def countAccents(str):
    count = 0
    for c in str:
        if c in accents:
            count += 1
    return count

def countAs(str):
    count = 0
    for c in str:
        if c in a_variants:
            count += 1
    return count

def features(X):
    
    F = np.zeros((len(X),5))
    for x in range(0,len(X)):
        F[x,0] = len(X[x])
        F[x,1] = countVowels(X[x])
        F[x,2] = countConsonants(X[x])
        F[x,3] = countAccents(X[x])
        F[x,4] = countAs(X[x])

    return F

def mytraining(f,Y):
    
    return clf
    
def mytrainingaux(f,Y,par):
    
    return clf

def myprediction(f, clf):
    Ypred = clf.predict(f)

    return Ypred