from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import json


class Watson:

    VERSION = '2018-05-01'
    APIKEY = 'CSh2ZtuxajP2OU0BzHOaRjx2O1KuLk7vV5Sh1SY9BeXs'
    URL = (
        'https://api.us-south.language-translator.watson.cloud.ibm.com/'
        'instances/f7c6534f-1703-4893-bf67-727dce6ec570'
    )


class Translator(Watson):

    def __init__(self):
        authenticator = IAMAuthenticator(
            __class__.APIKEY
        )
        self.language_translator = LanguageTranslatorV3(
            version=__class__.VERSION,
            authenticator=authenticator
        )

        language_translator.set_service_url(__class__.URL)

    def englishtofrench(self, text: str) -> str:
        response = self.language_translator.translate(
                        text=text,
                        model_id='en-fr'
                    ).get_result()

        return json.dumps(
            response,
            indent=2,
            ensure_ascii=False
        )


if __name__ == '__main__':
    translate = Translator()
    print(
        translate.english_to_french('Hello, how are you today?')
    )

# Take a screenshot of your function and save it as a .jpg or
# .png with the filename english_to_french

# Take a screenshot of your function and save it as a .jpg or
# .png with the filename english_to_german.
