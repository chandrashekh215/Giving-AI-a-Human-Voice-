from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def detect_emotion(text):
    result = classifier(text)[0]
    label = result['label']
    score = result['score']
    
    if label == "POSITIVE":
        emotion = "happy"
    elif label == "NEGATIVE":
        emotion = "frustrated"
    else:
        emotion = "neutral"
    
    return emotion, score
