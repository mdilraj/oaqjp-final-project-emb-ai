"""
This is sentiment analysis module
"""
import json
import requests

def sentiment_analyzer(text_to_analyze):
    """
    This is sentiment analyzer 
    it takes string as input and returns 
    label and score
    """
    url= ("https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/"
          "NlpService/SentimentPredict")
    headers= {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers = headers, timeout=30000)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    else:
        label = None
        score = None
    return {'label':label, 'score':score}
