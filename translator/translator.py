from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import json


class Watson:

    VERSION = '2018-05-01'
    APIKEY = 'CSh2ZtuxajP2OU0BzHOaRjx2O1KuLk7vV5Sh1SY9BeXs'
    URLROOT = 'https://api.us-south.language-translator.watson.cloud.ibm.com/'
    INSTANCE = 'instances/f7c6534f-1703-4893-bf67-727dce6ec570'

class Translator(Watson):

    def __init__(self):
        authenticator = IAMAuthenticator(
            __class__.APIKEY
        )
        self.language_translator = LanguageTranslatorV3(
            version=__class__.VERSION,
            authenticator=authenticator
        )
        self.language_translator.set_service_url(
            __class__.URLROOT + __class__.INSTANCE
        )

    def english_to_french(self, text: str) -> str:

        if text:
            response = self.language_translator.translate(
                            text=text,
                            model_id='en-fr'
                        ).get_result()

            return response,

        return {
                'error': 'Null Text',
                'message': 'There\'s no text informed to translate.'
            }

    def englishtogerman(self, text: str) -> str:

        if text:
            response = self.language_translator.translate(
                            text=text,
                            model_id='en-de'
                        ).get_result()

            return response,

        return {
                'error': 'Null Text',
                'message': 'There\'s no text informed to translate.'
            }
