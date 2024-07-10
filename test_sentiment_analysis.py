
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

import unittest

class TestSentimentAnalyzer(unittest.TestCase):

    def test_sentiment_analyzer(self):
        TESTCASE_1 = sentiment_analyzer('I love working with Python')
        TESTCASE_2 = sentiment_analyzer('I hate working with Pyhton')
        TESTCASE_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(TESTCASE_1["label"], 'SENT_POSITIVE')
        self.assertEqual(TESTCASE_2["label"], 'SENT_NEGATIVE')
        self.assertEqual(TESTCASE_3["label"], 'SENT_NEUTRAL')
    
    
unittest.main()


