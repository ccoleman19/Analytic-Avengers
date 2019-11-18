# AUTHOR:     Bilal Zuberi, Clay Coleman, Nick Luthman, Brandon Decker
# COURSE:     ISTM 615
# PROGRAM:    Project 10-4: Pig Latin Translator
# PURPOSE:    Create a program that translates a sentence into pig latin
#             
#
#

# INPUT:      Sentence in English from the console. 
#
# PROCESS:    Convert all English to lower case.  Remove and punctuation characters.
#             Conversion rules:
#             If a word starts with a vower, then add "way" t the end of the word.
#             If the word starts with a consonant, move all of the consonants before the
#             first vowel to the end of the word, then add "ay" to the end of the word.
#             If a word starts with the letter "y", then treat it like a consonant.
#


# OUTPUT:     Input test printed to the console.  The sentence is repeated with punctuation
#             Sentence converted in Pig latin in all its glory!
#
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.

# Beginning of the program below


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

