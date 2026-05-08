"""
This is emotion detection module
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """
    This is emotion detector method
    Takes text to analyze as input
    Returns emotion as output
    """
    url = ("https://sn-watson-emotion.labs.skills.network/v1/"
           "watson.runtime.nlp.v1/NlpService/EmotionPredict")
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers = headers, timeout=30000)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = ''
    max_score = 0
    for key in emotions:
        if emotions[key] > max_score:
            dominant_emotion = key
            max_score = emotions[key]

    emotions['dominant_emotion'] = dominant_emotion

    return emotions

