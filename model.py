#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from google_play_scraper import app, Sort, reviews
from transformers import pipeline

def gen_classifier():
    classifier = pipeline('sentiment-analysis', 
                      model="nlptown/bert-base-multilingual-uncased-sentiment")
    return classifier

def predict_stars(string):
    classifier = gen_classifier()
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

def extract_comments(app_id, num_comments):
    print(f"Extracting {num_comments} comments from app_id: {app_id}")
    rvws, token = reviews(
            app_id,                    # app's ID, found in app's url
            lang = 'es',               # defaults to 'en''
            sort = Sort.NEWEST,        # defaults to Sort.MOST_RELEVANT
            filter_score_with = None,  # defaults to None (get all scores)
            count = num_comments       # defaults to 100
        )
    return rvws

def create_comments_pdf(reviews_list, classifier, file_name = "reviews_file.csv"):
    print(f"Applying predictions over {len(reviews_list)} comments")
    model_starts_list = []
    model_score_list = []
    reviews_pdf = pd.DataFrame(reviews_list)
    results = classifier(list(reviews_pdf["content"]))
    for result in results:
        model_starts_list.append(result['label'])
        model_score_list.append(round(result['score'], 4))

    reviews_pdf["ModelStars"] = model_starts_list
    reviews_pdf["ModelStars"] = reviews_pdf["ModelStars"].apply(lambda x : int(x[0:1]))
    reviews_pdf["ModelScore"] = model_score_list
    reviews_pdf["StarsDifference"] = abs(reviews_pdf["score"] - reviews_pdf["ModelStars"])
    reviews_pdf.to_csv(file_name)
    return reviews_pdf

if __name__ == '__main__':
    comments_list = extract_comments("com.clarocolombia.miclaro", 200)
    comments_pdf = create_comments_pdf(comments_list, gen_classifier())
    print('Done')