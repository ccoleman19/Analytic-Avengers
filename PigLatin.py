

import string

def translateWord(textList):
    for word in textList:
        if word[0] in ('a','e', 'i','o', 'u'):
            newWord = word + 'way'
            print(newWord)
        
    

def wordList(text):
    removePunctuation = str.maketrans('','', string.punctuation)
    textList = text.translate(removePunctuation).split()
    print(translateWord(textList))
    print(textList)

def main():
    print('Pig Latin Translator\n\n')
    text = input('Enter Text:  ').lower()
    wordList(text)
    


if __name__ == '__main__':
    main()