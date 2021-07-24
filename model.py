#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from google_play_scraper import app, Sort, reviews
from transformers import pipeline

classifier = pipeline('sentiment-analysis', 
                      model="nlptown/bert-base-multilingual-uncased-sentiment")

def predict_stars(string):
    model_dict = classifier(string)
    model_dict = model_dict[0]
    if model_dict['label'] == '1 star':
        model_dict['Sentimiento'] = "Muy Negativo"
    elif model_dict['label'] == '2 stars':
        model_dict['Sentimiento'] = "Negativo"
    elif model_dict['label'] == '3 stars':
        model_dict['Sentimiento'] = "Neutro"
    elif model_dict['label'] == '4 stars':
        model_dict['Sentimiento'] = "Positivo"
    else:
        model_dict['Sentimiento'] = "Muy Positivo"
    return model_dict

if __name__ == '__main__':
    rvws, token = reviews(
            'com.clarocolombia.miclaro', # app's ID, found in app's url
            lang='es',            # defaults to 'en''
            sort=Sort.NEWEST,     # defaults to Sort.MOST_RELEVANT
            filter_score_with = None,  # defaults to None (get all scores)
            count = 10000          # defaults to 100
        )

    reviews_pdf = pd.DataFrame(rvws)
    model_starts_list = []
    model_score_list = []
    results = classifier(list(reviews_pdf["content"]))
    for result in results:
        model_starts_list.append(result['label'])
        model_score_list.append(round(result['score'], 4))


    reviews_pdf["ModelStarts"] = model_starts_list
    reviews_pdf["ModelStarts"] = reviews_pdf["ModelStarts"].apply(lambda x : int(x[0:1]))
    reviews_pdf["ModelScore"] = model_score_list
    reviews_pdf["StartsDifference"] = abs(reviews_pdf["score"] - reviews_pdf["ModelStarts"])
    reviews_pdf.to_csv('reviews_file.csv')

