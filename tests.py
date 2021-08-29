"""
Test Module
"""
import unittest

from translator.translator import Translator


class TestEnglishToFrench(unittest.TestCase):

    """
    Testing class for testint english translation of
    IBM WATSON API
    """

    def setUp(self):
        self.translate = Translator()

    def test_if_response_is_null(self):
        response = self.translate.english_to_french('')

        self.assertEqual(
            'Null Text',
            response.get(
                'error', ''
            )
        )

    def test_translate_hello(self):
        response = self.translate.english_to_french('Hello')
        hello_translated = response[0]['translations'][0]['translation']

        self.assertEqual(
            'Bonjour',
            hello_translated
        )

    def test_word_counting(self):
        text = 'Python and Artificial Inteligence'
        response = self.translate.english_to_french(text)
        word_count = response[0]['word_count']

        self.assertEqual(
            len(text.split()),
            word_count
        )

class TestEnglishToGerman(unittest.TestCase):

    """
    Testing class for testint english translation of
    IBM WATSON API
    """

    def setUp(self):
        self.translate = Translator()

    def test_if_response_is_null(self):
        response = self.translate.englishtogerman('')

        self.assertEqual(
            'Null Text',
            response.get(
                'error', ''
            )
        )

    def test_translate_hello(self):
        response = self.translate.englishtogerman('Hello')
        hello_translated = response[0]['translations'][0]['translation']

        self.assertEqual(
            'Hallo',
            hello_translated
        )

    def test_word_counting(self):
        text = 'Python and Artificial Inteligence'
        response = self.translate.englishtogerman(text)
        word_count = response[0]['word_count']

        self.assertEqual(
            len(text.split()),
            word_count
        )
