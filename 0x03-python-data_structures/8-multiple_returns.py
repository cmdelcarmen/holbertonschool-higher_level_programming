#!/usr/bin/python3


def multiple_returns(sentence):

    if len(sentence) == 0:
        sentence += 'None'

    print(len(sentence))

    lengthOfSentence = len(sentence)
    firstLetterOfSentence = sentence[0]

    sentence_tuple = lengthOfSentence, firstLetterOfSentence

    return sentence_tuple
