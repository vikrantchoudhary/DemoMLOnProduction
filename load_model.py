import pickle

with open("model.p", "rb") as f:
    model = pickle.load(f)

sample_texts = [
    "Data natives has many great workshops. I love it!",
    "The connection is so bad, I can not understand anything!",
]

result = model.predict_proba(sample_texts)
print(result)