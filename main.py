"""
Main Module
"""

from translator.translator import Translator

if __name__ == '__main__':

    translate = Translator()
    
    sample = (
        'Mr. and Mrs. Dursley of number four, '
        'Privet Drive, were proud to say that '
        'they were perfectly normal, thank you '
        'very much.'
    )

    print(
        translate.english_to_french(sample)
    )
    print(
        translate.englishtogerman(sample)
    )
    
