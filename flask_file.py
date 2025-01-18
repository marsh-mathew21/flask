import pandas as pd
import numpy as np

df=pd.read_csv("train_csv.csv")

df.head()

df["Gender"] =df["Gender"].map({"Male":0,"female":1}) 
df["Married"]=df["Married"].map({"yes":1,"No":0})
df["Loan_Status"]=df["Loan_Status"].map({"Y":1,"N":0})

df=df.dropna()

df.isnull().sum()

df.head()


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(df[["Gender","Married","ApplicantIncome","LoanAmount","Credit_History"]],df["Loan_Status"],test_size=0.2,random_state=42)

from sklearn import linear_model

model=linear_model.LogisticRegression()

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_pred)

import pickle

pickle_out=open("classifier.pkl",mode="wb")

pickle.dump(model,pickle_out)

pickle_out.close()

