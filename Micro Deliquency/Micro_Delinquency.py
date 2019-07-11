'''
Data Deliquency Project

Please red the document file for the project information.

Download data from this link-
https://drive.google.com/file/d/1NLSYOpgGfpnD2ojJlklFmHcicuV3prko/view?usp=sharing

Same link is given in document.

The highest frequency comes when we select the data with Univariate Feature Selection method (1st Method)
and the algorithm is Gradient Boosting Classifier with accuracy of 90.33%.
You can comment the other methods in the acuu function except Gradient Boosting Classifier beacouse they
are only for checking accuracy, othersiwse the program can take upto 30 minutes to
to give the final output.
Thankyou.
'''
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 1000)
pd.set_option('display.max_column', 40)
pd.set_option('precision', 2)

import warnings

warnings.filterwarnings("ignore")

train = pd.read_csv("Micro_delinquency_train_test_dataset_v2.csv")

test = pd.read_csv("Micro_delinquency_train_test_dataset_v2.csv")
train1 = train.drop(["label"], axis=1)
test1 = test.drop(["label"], axis=1)
train1.drop(["pdate"], axis=1)
col = train1.columns
col1 = test1.columns
train1[col] = train1[col].apply(pd.to_numeric, errors="coerce")
test1[col1] = test1[col].apply(pd.to_numeric, errors="coerce")
train1= train1.drop(['pcircle'], axis=1)
train1= train1.drop(['pdate'], axis=1)
train1= train1.drop(['msisdn'], axis=1)
test1= test1.drop(['pcircle'], axis=1)
test1= test1.drop(['pdate'], axis=1)
test1= test1.drop(['msisdn'], axis=1)
train1 = train1.fillna(train1.mean())
test1 = test1.fillna(train1.mean())
train1 = abs(train1)
test1 = abs(test1)

from sklearn.preprocessing import Normalizer
n= Normalizer()
n.fit(train1)
train1 = n.fit_transform(train1)

def acuu(x ,y):
    l =[]
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.33, random_state=7)

    # MODEL-1) LogisticRegression
    # ------------------------------------------
    from sklearn.linear_model import LogisticRegression

    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)
    y_pred = logreg.predict(x_val)
    acc_logreg = round(accuracy_score(y_pred, y_val) * 100, 2)
    print("MODEL-1: Accuracy of LogisticRegression : ", acc_logreg)
    l.append(acc_logreg)



    # MODEL-2) Gaussian Naive Bayes
    # ------------------------------------------
    from sklearn.naive_bayes import GaussianNB

    gaussian = GaussianNB()
    gaussian.fit(x_train, y_train)
    y_pred = gaussian.predict(x_val)
    acc_gaussian = round(accuracy_score(y_pred, y_val) * 100, 2)
    print("MODEL-2: Accuracy of GaussianNB : ", acc_gaussian)
    l.append(acc_gaussian)



    # MODEL-3) Support Vector Machines
    # ------------------------------------------
    from sklearn.svm import SVC

    svc = SVC()
    svc.fit(x_train, y_train)
    y_pred = svc.predict(x_val)
    acc_svc = round(accuracy_score(y_pred, y_val) * 100, 2)
    print("MODEL-3: Accuracy of Support Vector Machines : ", acc_svc)
    l.append(acc_svc)



    # MODEL-4) Linear SVC
    # ------------------------------------------
    from sklearn.svm import LinearSVC

    linear_svc = LinearSVC()
    linear_svc.fit(x_train, y_train)
    y_pred = linear_svc.predict(x_val)
    acc_linear_svc = round(accuracy_score(y_pred, y_val) * 100, 2)
    print("MODEL-4: Accuracy of LinearSVC : ", acc_linear_svc)
    l.append(acc_linear_svc)



    # MODEL-5) Perceptron
    # ------------------------------------------
    from sklearn.linear_model import Perceptron

    perceptron = Perceptron()
    perceptron.fit(x_train, y_train)
    y_pred = perceptron.predict(x_val)
    acc_perceptron = round(accuracy_score(y_pred, y_val) * 100, 2)
    print("MODEL-5: Accuracy of Perceptron : ", acc_perceptron)
    l.append(acc_perceptron)



    # MODEL-6) Decision Tree Classifier
    # ------------------------------------------
    from sklearn.tree import DecisionTreeClassifier

    decisiontree = DecisionTreeClassifier()
    decisiontree.fit(x_train, y_train)
    y_pred = decisiontree.predict(x_val)
    acc_decisiontree = round(accuracy_score(y_pred, y_val) * 100, 2)
    print("MODEL-6: Accuracy of DecisionTreeClassifier : ", acc_decisiontree)
    l.append(acc_decisiontree)



    # MODEL-7) Random Forest
    # ------------------------------------------
    from sklearn.ensemble import RandomForestClassifier

    randomforest = RandomForestClassifier()
    randomforest.fit(x_train, y_train)
    y_pred = randomforest.predict(x_val)
    acc_randomforest = round(accuracy_score(y_pred, y_val) * 100, 2)
    print("MODEL-7: Accuracy of RandomForestClassifier : ", acc_randomforest)
    l.append(acc_randomforest)



    # MODEL-8) KNN or k-Nearest Neighbors
    # ------------------------------------------
    from sklearn.neighbors import KNeighborsClassifier

    knn = KNeighborsClassifier()
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_val)
    acc_knn = round(accuracy_score(y_pred, y_val) * 100, 2)
    print("MODEL-8: Accuracy of k-Nearest Neighbors : ", acc_knn)
    l.append(acc_knn)

    # OUTPUT:-
    # MODEL-8: Accuracy of k-Nearest Neighbors :  77.66

    # MODEL-9) Stochastic Gradient Descent
    # ------------------------------------------
    from sklearn.linear_model import SGDClassifier

    sgd = SGDClassifier()
    sgd.fit(x_train, y_train)
    y_pred = sgd.predict(x_val)
    acc_sgd = round(accuracy_score(y_pred, y_val) * 100, 2)
    print("MODEL-9: Accuracy of Stochastic Gradient Descent : ", acc_sgd)
    l.append(acc_sgd)



    # MODEL-10) Gradient Boosting Classifier
    # ------------------------------------------
    from sklearn.ensemble import GradientBoostingClassifier

    gbk = GradientBoostingClassifier()
    gbk.fit(x_train, y_train)
    y_pred = gbk.predict(x_val)
    acc_gbk = round(accuracy_score(y_pred, y_val) * 100, 2)
    print("MODEL-10: Accuracy of GradientBoostingClassifier : ", acc_gbk)
    l.append(acc_gbk)

# 1) Univarite Feature Selection
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

test = SelectKBest(score_func=chi2, k=11)        # k is number of features
fit = test.fit(train1, train["label"])
train2 = test.transform(train1)
acuu(train2, train["label"])

# 2) Recursive Feature Elimination

from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

model = LogisticRegression()
rfe = RFE(model, 11)
fit = rfe.fit(train1, train["label"])     
train2 = fit.transform(train1)
acuu(train2, train["label"])

# 3) Principal Component Analysis

from sklearn.decomposition import PCA
pca = PCA(11)
fit = pca.fit(train1, train["label"])
train2 = pca.transform(train1)
acuu(train2, train["label"])




