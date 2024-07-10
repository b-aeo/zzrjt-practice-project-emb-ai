'''This is the Sentiment Analysis Module code calls the Watson AI api'''
import json
import requests



def sentiment_analyzer(text_to_analyse):
    '''This is the function'''
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/\
    watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = {"raw_document": { "text": text_to_analyse }}
    response = requests.post(url, json = myobj, headers=headers, timeout = 30)
    if response.status_code == 500:
        label = None
        score = None
        return {'label' : label, 'score' : score}
    if response.status_code == 200:
        format_response = json.loads(response.text)
        final_response = format_response['documentSentiment']
        return final_response
