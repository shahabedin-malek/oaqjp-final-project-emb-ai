"""
Emotion Detection module using Watson NLP Embed library.
"""
import requests


def emotion_detector(text_to_analyse):
    """
    Detects emotions in the given text using Watson NLP Embed library.

    Args:
        text_to_analyse (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary with emotion scores and the dominant emotion.
    """
    if text_to_analyse is None or text_to_analyse.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_json = response.json()

    emotions = response_json.get(
        'emotionPredictions', [{}]
    )[0].get('emotion', {})

    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores
