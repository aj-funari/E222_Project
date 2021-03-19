from sklearn import datasets
from joblib import load
import numpy as np
import json

#load the model

my_model = load('logistic.pk1')

def my_prediction(arg):
    dummy = np.array(arg)
    dummyT = dummy.reshape(1,-1)
    a = dummy.shape
    b = dummyT.shape
    a_str = json.dumps(a)
    b_str = json.dumps(b)
    prediction = my_mdl.predict(dummyT)
    return(prediction)

def score(test_size):
    x_train, x_test, y_train, y_test = train_test_split(X_new, Y_new, test_size, random_state=0)
    my_mdl = pipe.fit(x_train, y_train)
    score = my_mdl.score(x_test,y_test)
    return(score)