#!/usr/bin/env python
# coding: utf-8

from typing import Optional
from fastapi import FastAPI
import pandas as pd
from model import predict_stars

comments_df = pd.read_csv("reviews_file.csv")
comments_df = comments_df.sort_values(by = "repliedAt", ascending = False)
comments_df = comments_df.loc[:,["content","ModelStars"]]
comments_df = comments_df.reset_index(drop = True)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Easy Data"}


@app.get("/comments/{item_id}")
def read_pandas_df(item_id: int, q: Optional[str] = None):
    return comments_df.loc[0:item_id - 1,:].to_dict()


@app.get("/predict/")
def predict_string(text: Optional[str] = None):
    return predict_stars(text)
