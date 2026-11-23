"""Detect emotions from English text using the IBM Watson NLP endpoint."""

import requests


EMOTION_ENDPOINT = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
EMOTION_MODEL = "emotion_aggregated-workflow_lang_en_stock"
EMOTION_NAMES = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return five emotion scores and the dominant emotion for *text_to_analyze*.

    An invalid/empty request (HTTP 400) returns six ``None`` values.
    Other HTTP failures and unexpected response formats raise exceptions.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return {**dict.fromkeys(EMOTION_NAMES), "dominant_emotion": None}

    response = requests.post(
        EMOTION_ENDPOINT,
        headers={"grpc-metadata-mm-model-id": EMOTION_MODEL},
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30,
    )
    if response.status_code == 400:
        return {**dict.fromkeys(EMOTION_NAMES), "dominant_emotion": None}

    response.raise_for_status()
    predictions = response.json()["emotionPredictions"]
    emotions = predictions[0]["emotion"]
    scores = {name: emotions[name] for name in EMOTION_NAMES}
    scores["dominant_emotion"] = max(EMOTION_NAMES, key=scores.get)
    return scores
