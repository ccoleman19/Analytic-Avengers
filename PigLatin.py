import string


def translateWord(textList):
    newWords = []
    for word in textList:
        if word[0] in "aeiou":
            newWord = word + "way"
            newWords.append(newWord)
        else:
            fVowel = firstVowel(word)
            beginning = word[0:fVowel]
            ending = word[fVowel:]
            newWord = ending + beginning + "ay"
            newWords.append(newWord)
    return newWords


def firstVowel(word):
    try:
        vowelList = []
        for l in "aeiouy":
            vowel = word.find(l)
            if vowel > 0:
                vowelList.append(vowel)
        return min(vowelList)
    except ValueError:
        pass


def logging():
    pass

def wordList(text):
    removePunctuation = str.maketrans("", "", string.punctuation)
    text = text.translate(removePunctuation)
    textList = text.translate(removePunctuation).split()
    return textList, text


def unpackList(listWords):
    newSentance = ""
    for word in listWords:
        newSentance += word + " "
    return newSentance


def redo():
    redo = input("Continue? (y/n): ").lower()
    if redo == "y":
        main()
    else:
        print("\n\nGood Bye!")


def main():
    print("Pig Latin Translator\n\n")
    text = input("Enter Text:  ").lower()
    print("English:     " + wordList(text)[1])
    pLatinWords = translateWord(wordList(text)[0])
    print("Pig Latin:   " + unpackList(pLatinWords))
    print()
    redo()


if __name__ == "__main__":
    main()
