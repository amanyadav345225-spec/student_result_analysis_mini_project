

import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("results_analysis.csv")

print(df.head())

df['Pass_Fail'] = df['Pass_Fail'].map({
    True: 1,
    False:0
})

df.drop(['Results'],axis='columns')

print(df.sample(5))

"""pass_fail ke sath percentage bhi drop krna h qki model directly mathematical rule learn kar rha h

"""

input = df.drop(['Pass_Fail','Percentage','Results','Total'],axis='columns')
output = df['Pass_Fail']

print(input.head())

print(output.head())

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(input,output,test_size = 0.2,random_state=42)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train= scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report,f1_score,recall_score,precision_score
print("confusion matrix : \n",confusion_matrix(y_test,y_pred))
print("accuracy  : ",accuracy_score(y_test,y_pred))
print("classification report : \n",classification_report(y_test,y_pred))

print(input.columns.tolist())
print("Percentage" in input.columns)

print("Train:", model.score(X_train, y_train)*100)
print("Test:", model.score(X_test, y_test)*100)

"""KNN classifier on the same model"""

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

y_pred_knn = knn.predict(X_test)

print(f"accuracy : {accuracy_score(y_test,y_pred_knn)*100}")

"""comparing both logistic regression and kNN accuracy

"""

print("Logistic Regression:",
      accuracy_score(y_test, y_pred)*100)

print("KNN:",
      accuracy_score(y_test, y_pred_knn)*100)

"""for multiple k values in KNN

"""

for k in [3, 5, 7, 9, 11]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    train_acc = knn.score(X_train, y_train)
    test_acc = knn.score(X_test, y_test)

    print(f"k={k}, Train={train_acc:.3f}, Test={test_acc:.3f}")

print(" logistic confusion matrix : \n",confusion_matrix(y_test,y_pred))

print("KNN confusion matrix \n",confusion_matrix(y_test,y_pred_knn))

#confusion matrix for multiple k values in knn
for k in (3,5,7,8,11):
  nn = KNeighborsClassifier(n_neighbors=k)
  knn.fit(X_train,y_train)
  y_pred_knn = knn.predict(X_test)
  print(f"for k = {k} confusion mat \n {confusion_matrix(y_test,y_pred_knn)}")