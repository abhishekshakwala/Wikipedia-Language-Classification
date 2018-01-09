
def decisionStump(inputSentence, wordArray):
    valueENDU = [6.954559846999833, 5.174871725327455, 3.87558504576811, 4.004342231396382, 3.493943638484824, 3.0738013867669323]
    
    resultENDU = adaDecision("ENDU", valueENDU, inputSentence, wordArray)
    if resultENDU < 0:
        return "DUTCH"
    else:
        return "ENGLISH"
    
def adaDecision(language, valueENDU, inputSentence, word):
    checkSum = 0
    resultENDU = []
    if language == "ENDU":
        if "de" in word or "het" in word or "dat" in word or "en" in word or "een" in word or "voor" in word or "van" in word or "welke" in word or "te" in word or "hij" in word or "zij" in word or "op" in word or "ik" in word or "bij" in word:
            resultENDU.append(1)
        else:
            resultENDU.append(-1)
        if "the" in word or "but" in word or "for" in word or "which" in word or "that" in word or "and" in word or "not" in word or "to" in word or "in" in word:
            resultENDU.append(-1)
        else:
            resultENDU.append(1)
        if "aa" in inputSentence or "ee" in inputSentence or "ii" in inputSentence or "uu" in inputSentence:
            resultENDU.append(1)
        else:
            resultENDU.append(-1)
        if "ijk" in inputSentence or "sch" in inputSentence or "ijn" in inputSentence:
            resultENDU.append(1)
        else:
            resultENDU.append(-1)
        if "is" in word or "of" in word or "was" in word or "all" in word:
            resultENDU.append(-1)
        else:
            resultENDU.append(1)
        if "he" in word or "she" in word or "it" in word or "they" in word:
            resultENDU.append(-1)
        else:
            resultENDU.append(1)
            
        for i in resultENDU:
            checkSum += valueENDU[i] * resultENDU[i]
        return checkSum

if __name__ == '__main__':
    inputSentence = input("Enter the sentence you want to predict")
    wordArray = inputSentence.split()
    results = decisionStump(inputSentence, wordArray)
    print(results)
