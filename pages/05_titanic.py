import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

st.dataframe(df)

st.code('''
import pickle
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df.dropna(inplace=True)

df.loc[df['Sex'] == "female", 'Sex'] = 0
df.loc[df['Sex'] == "male", 'Sex'] = 1

X = df[["Sex", "Age", "SibSp", "Parch"]]

y = df["Survived"]

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)

filename = 'model.sav'
pickle.dump(clf, open(filename, 'wb'))''')

# st.write(clf.predict([[1, 1, 1, 1]]))