import requests
import json

def emotion_detector(text_to_analyse):
    try:
       if len(text_to_analyse) <= 4:
          return {"message":"It's mandatori the text to analyse please sending"}, 400

       url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
       header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
       input_json = { "raw_document": { "text": text_to_analyse } }
       response = requests.post(url, json = input_json, headers=header)
       data = response.json()
       sentiment = data['documentSentiment']['sentimentMentions'][0]['sentimentprob']
       
       print(sentiment)
       sum_percentages  = 0 
       for emotion in sentiment:
           sum_percentages  = sum_percentages + sentiment[emotion]
       # Calculate the porcentaje remaining
       remaining = 1 - sum_percentages
       print(remaining)
       # for emotion in sentiment:
       # assignment of values ​​for the totals of each sentiment
       anger_score = remaining * 0.4  # 20% del porcentajeremaining
       disgust_score = remaining * 0.3  # 20% del porcentajeremaining
       fear_score = remaining * 0.2  # 20% del porcentajeremaining
       joy_score = remaining * 0.1  # 20% del porcentajeremaining
       sadness_score = remaining * 0.1  # 20% del porcentajeremaining
       
       emotionsOut = {
           'anger':anger_score,
           'disgust': disgust_score,
           'fear': fear_score,
           'joy': joy_score,
           'sadness': sadness_score,
           'dominant_emotion': 'joy' if data['documentSentiment']['label']  == 'SENT_POSITIVE'  else ('sadness' if data['documentSentiment']['label']  == 'SENT_NEGATIVE'  else 'anger')
       }
    
       return  {"message":emotionsOut}, 200
    except requests.exceptions.RequestException as e:
       # Handle general request exceptions
       error = "An error occurred during the request"
       print(f"{error}: {e}")
       return {"message":emotionsOut}, 500
