from tkinter import X
from pydantic.dataclasses import dataclass
import json
import pandas as pd

from joblib import load

from typing import Union

from fastapi import FastAPI
from sklearn.metrics import mean_squared_error

from DataModel import DataModel

from DataModelScore import DataModelScore


app = FastAPI()


@app.get("/")
def read_root():
    
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/predict")
def make_predictions(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    model = load("assets/modelo.joblib")
    result = model.predict(df)
    return result.tolist()

@app.post("/score")
def determine_score(dataModelScore: DataModelScore):
    df = pd.DataFrame(dataModelScore.dict(), columns=dataModelScore.dict().keys())
    df.columns = dataModelScore.columns()
    model = load("assets/modelo.joblib")
    x = df.drop('Admission Points', axis = 1)
    y = df['Admission Points']
    model.fit(x,y)
    pred = model.predict(x)
    result = mean_squared_error(y,pred)
    return [result]

