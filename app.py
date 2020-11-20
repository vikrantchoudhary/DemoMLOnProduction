from fastapi import FastAPI
import pickle

app = FastAPI()

@app.get("/")
async def root(demo: str="default") :
    return { "message " : f"testing message {demo}"}


@app.get("/predict")
async  def predict(text: str) :
    with open("model.p","rb") as f:
        pipe = pickle.load(f)
    result = pipe.predict_proba([text])
    return {"text" : text , "result " : result[0,1]}

with open("model.p","rb") as f:
        pipe = pickle.load(f)

@app.get("/predict_fast")
async  def predict(text: str) :
    result = pipe.predict_proba([text])
    return {"text" : text , "result " : result[0,1]}

