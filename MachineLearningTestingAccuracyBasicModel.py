from pathlib import  Path

path = Path()
for file in path.glob('*.py'):
    print(file)
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music = pd.read_csv("Music.csv")
X = music.drop(columns = ["Genre"])
Y = music["Genre"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
predictions = model.predict(X_test)
score = accuracy_score(predictions, Y_test)
score