import glob
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

text_pos = []
for file_name in glob.glob("aclImdb/train/pos/*"):
    with open(file_name, "r") as file:
        text_pos.append(file.read())
text_neg = []
for file_name in glob.glob("aclImdb/train/neg/*"):
    with open(file_name, "r") as file:
        text_neg.append(file.read())

df_pos = pd.DataFrame(text_pos, columns=["text"])
df_pos["target"] = 1
df_neg = pd.DataFrame(text_neg, columns=["text"])
df_neg["target"] = 0
df = pd.concat([df_pos, df_neg])

pipe = Pipeline(
    [
        ("tfidf", TfidfVectorizer()),
        ("cls", RandomForestClassifier()),
    ]
)

X, y = df["text"], df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
pipe.fit(X_train, y_train)

with open("model.p", "wb") as f:
    pickle.dump(pipe, f)

print("Model saved")