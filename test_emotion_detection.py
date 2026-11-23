"""Unit tests for the Watson NLP EmotionDetection package.

Responses are mocked to test our parsing logic reliably and without network.
For a live Watson NLP check, follow the commands in README.md.
"""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify the dominant emotion across the five required categories."""

    def assert_detects(self, text, expected_emotion):
        """Mock Watson NLP and check returned scores and dominant emotion."""
        emotions = {
            "anger": 0.05,
            "disgust": 0.05,
            "fear": 0.05,
            "joy": 0.05,
            "sadness": 0.05,
        }
        emotions[expected_emotion] = 0.80
        fake_response = Mock(status_code=200)
        fake_response.json.return_value = {
            "emotionPredictions": [{"emotion": emotions}]
        }
        with patch("EmotionDetection.emotion_detection.requests.post", return_value=fake_response):
            actual = emotion_detector(text)
        self.assertEqual(actual["dominant_emotion"], expected_emotion)
        for emotion in emotions:
            self.assertEqual(actual[emotion], emotions[emotion])

    def test_joy(self):
        """Validate the joy response."""
        self.assert_detects("I am glad this happened", "joy")

    def test_anger(self):
        """Validate the anger response."""
        self.assert_detects("I am really mad about this", "anger")

    def test_disgust(self):
        """Validate the disgust response."""
        self.assert_detects("I feel disgusted just hearing about this", "disgust")

    def test_sadness(self):
        """Validate the sadness response."""
        self.assert_detects("I am so sad about this", "sadness")

    def test_fear(self):
        """Validate the fear response."""
        self.assert_detects("I am really afraid that this will happen", "fear")

    def test_http_400(self):
        """Return None values if the Watson service rejects an input."""
        fake_response = Mock(status_code=400)
        with patch("EmotionDetection.emotion_detection.requests.post", return_value=fake_response):
            actual = emotion_detector("bad input")
        self.assertEqual(actual, {
            "anger": None, "disgust": None, "fear": None,
            "joy": None, "sadness": None, "dominant_emotion": None,
        })


if __name__ == "__main__":
    unittest.main()
