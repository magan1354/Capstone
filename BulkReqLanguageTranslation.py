# Author: Sharad Agrawal
# Bulk translation request.
''' Input:
This script takes input as comma (,) seperated list of source string
and destination laguage code in which user want to translate source.
Source language will be auto detected by googletrans.
Ex:
Input:
Enter list of source string:안녕 친구,Welcome on Codeproject
Enter destination language:ja

Output:
안녕 친구  (Src= ko ) ->  こんにちは友人
Welcome on Codeproject  (Src= en ) ->  Codeprojectへようこそ

'''

# Import Package
from googletrans import Translator

# Create Translator object
translator = Translator()

# Take Input
line = input('Enter list of source string:')
dstLang = input('Enter destination language:')

# Convert source line into list
lineList = line.split(',')

# Perform translation
translatedList = translator.translate(lineList, dest=dstLang)

# Print output
for translated in translatedList:
    print(translated.origin, ' (Src=',translated.src, ') -> ', translated.text)

