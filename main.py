from typing import Optional
from fastapi import FastAPI
import pandas as pd

df = pd.read_csv("reviews_file.csv")
final_df = df.loc[:,["content","ModelStarts"]]

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Easy Data"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/comments/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return final_df.loc[0:item_id,:].to_dict()