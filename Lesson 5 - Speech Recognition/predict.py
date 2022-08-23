import requests

modelID = None
api = None

def set_model_ID(model_ID):
    global modelID, api
    modelID = model_ID
    api = 'https://aicode101.com/api/model/%s/predict' % (modelID)

def classify(term):
    terms = [term]
    httpResponse = requests.post(api, json={'testingSet': terms})
    response = httpResponse.json()
    return response

def text_classify(term):
    response = classify(term)
    predictions = response['predictions'][0]
    label = predictions['label']
    confidence = predictions['confidences'][predictions['label']] * 100
    return label, confidence
    