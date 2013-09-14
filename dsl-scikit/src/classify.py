#!/usr/bin/python
import copper
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

dft = pd.read_csv("../data/train.csv", header=None)
dfn = pd.read_csv("../data/trainLabels.csv",header=None)
training_data = pd.concat([dft,dfn],axis=1,ignore_index=True)
train = copper.Dataset(training_data)
train.role[40] = train.TARGET


testing_data = pd.read_csv("../data/test.csv", header=None)
test = copper.Dataset(testing_data)
print train.metadata
#print test.metadata

mc = copper.ModelComparison()
#mc['LR'] = LogisticRegression() #Got a accuracy of 0.80179
#mc['LR with p=l1'] = LogisticRegression(penalty='l1') #Got an accuracy of 0.80551
mc['SVM']=SVC(probability=True) #Got an accuracy of 0.91282
mc.set_train(train)
#mc.get_test(test)
mc.fit()
df = mc.predict(copper.t.ml_inputs(test))
df.index = [i+1 for i in range(9000)]
df.to_csv("../data/result.csv",header=["Solution"],index_label="Id")
