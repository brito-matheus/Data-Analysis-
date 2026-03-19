# Metodo de classificacao Binario 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', version=1)

# Checking the format 

type(mnist)
mnist.keys()
mnist.DESCR
x , y = mnist["data"].values, mnist["target"].values

# y is the outcome 
# x is the vector of features
y = y.astype(float)
y

# Visualization of the data
plt.imshow(x[10].reshape(28, 28), cmap="binary")

for i in range(10):
    print(i)
    plt.imshow(x[i].reshape(28, 28), cmap="binary")

# Importing other modules for the classification task

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Objective: Create a binary classifier to determine if the digit is 5 or not
y_train_5 = (y_train == 5)

pd.Series(y_train_5).value_counts()

# Importing the classifier 
from sklearn.linear_model import SGDClassifier
from sklearn import linear_model as lm


sgdc_classifier = SGDClassifier()
sgdc_classifier.fit(x_train, y_train_5)
type(sgdc_classifier)


sgdc_classifier.predict(x_train[0].reshape(1, -1))

# Metrics to check the performance of the classifier
from sklearn.model_selection import cross_val_score

# Make the accurary of the classifier using the cross validation method
cross_val_score(
    sgdc_classifier, x_train, y_train_5, cv=3, scoring="accuracy"
)

# Checking the confusion matrix of the classifier 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report

confusion_matrix(y_train_5, sgdc_classifier.predict(x_train))

# Making the y_pred 
y_pred = sgdc_classifier.predict(x_train)

print(
    classification_report(y_train_5, y_pred)
)

# making it multiple class 
sgdc_classifier_complete = SGDClassifier()
sgdc_classifier_complete.fit(x_train, y_train)

# Checking the prediction 
n = 10

plt.imshow(x_train[n].reshape(28, 28), cmap="binary")

# Predicted
sgdc_classifier_complete.predict([x_train[n]])

# Make multiple cross-validation
from sklearn.model_selection import cross_val_predict 
y_train_pred = cross_val_predict(sgdc_classifier_complete, X=x_train,y=y_train, cv=3)


# Checking the quality of the prediction
print(confusion_matrix(y_train, y_train_pred))
print(classification_report(y_train, y_train_pred))

# Make the precision in classification report and make a bar plot
import seaborn as sns

cfn_matrix  = confusion_matrix(y_train, y_train_pred)

fig, ax = plt.subplots(figsize = (25, 8))
sns.heatmap(cfn_matrix, annot=True, fmt='.0f', cmap='binary')


#### Modelos the Machine Learning 

%reset -sf

import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np


# Linear Model 

x = np.random.rand(100)
y = 0.4 + 2.5 * x + np.random.rand(100)

m_x = np.c_[np.ones((100, 1)), x]

# Making the betas 
thetas = np.linalg.inv(m_x.T.dot(m_x)).dot(m_x.T).dot(y)
print(thetas)
print([0.4, 2.5])

y_pred = m_x.dot(thetas)

fig, ax = plt.subplots(figsize = (25,8))
plt.scatter(x, y)
plt.plot(x, y_pred, color='r', marker='o')

# Gradient Descent 
eta = 0.1
n_interaction = 10
m = 100

theta_gd = np.random.rand(2,1)
fig, ax = plt.subplots(figsize=(25,8))
plt.scatter(x, y) 

range(10)

for interaction in range(n_interaction):
    gradient = 2/m * m_x.T.dot(m_x.dot(theta_gd) - y)
    theta_gd = theta_gd -  eta * gradient
    y_hat = m_x.dot(theta_gd)

    ax.plot(x, y_hat, alpha = 0.1 + interaction/n_interaction)


## Regressoes 

y_quad =  3 * x **2  + 2*x + np.random.rand(100)
# checking


fig, ax = plt.subplots(figsize = (25,8))
plt.scatter(x, y_quad, color = 'r')

m_x_quad = np.c_[np.ones((100, 1)), x, x**2]