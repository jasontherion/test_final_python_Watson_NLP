from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    
    def test_sentiment_analyzer_joy(self):
        result_1 = sentiment_analyzer('I am glad this happened')
        self.assertEqual(result_1['joy'], 'joy')

    def test_sentiment_analyzer_anger(self):
        result_1 = sentiment_analyzer('I am really mad about this')
        self.assertEqual(result_1['anger'], 'anger')

    def test_sentiment_analyzer_disgust(self):
        result_1 = sentiment_analyzer('I feel disgusted just hearing about this')
        self.assertEqual(result_1['disgust'], 'disgust')

    def test_sentiment_analyzer_sadness(self):
        result_1 = sentiment_analyzer('I am so sad about this')
        self.assertEqual(result_1['sadness'], 'sadness')

    def test_sentiment_analyzer_fear(self):
        result_1 = sentiment_analyzer('I am really afraid that this will happen')
        self.assertEqual(result_1['fear'], 'fear')

    if __name__ == '__main__':
       unittest.main()