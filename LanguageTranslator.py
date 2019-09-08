# Author:Sharad Agrawal :)
# Language Translator
'''
This scrict provides two functionalities.
1. Language translation: User need to insert source string, source language and destination language
code as input. User will get translated string as output.

2. Language Detection: User need to insert source string as input. User will get detect language
code and confidence as output.

'''
# Import Package
from googletrans import Translator

# Create Translator object
translator = Translator()

while True:
    print('\n-------------------------------------')
    print('Choose Option (Press 0 to exit)')
    print('1. Language Translation')
    print('2. Language Detection')

    option = int(input('Option:'))

    if option==1:
        srcString = input('Enter source string:')
        srcLang = input('Enter source language:')
        dstLang = input('Enter destination language:')

        # Translate source string in request destination laguage
        translated = translator.translate(srcString, src= srcLang, dest=dstLang)

        # Print source string
        print('Source string:'+ translated.origin)

        # Print source language
        print('Source Language:'+ translated.src)

        # Print translated string
        print('Translated string:'+ translated.text)

        # Print destination laguage
        print('Destination Language:'+ translated.dest)

        # Print translated string pronumciation
        print('Destination pronunciation:', translated.pronunciation)
    elif option==2:
        srcString = input('Enter source string:')
        
        # Translate source string in request destination laguage
        detected = translator.detect(srcString)

        # Print detected language
        print('Detected Language:', detected.lang, ' with confidence: ', detected.confidence)
    elif option==0:
        break
    else:
        print('Invalid option')

