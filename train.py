import csv
import math

def calculateImpurity(value, instances):
    p1 = []
    p2 = []
    p1_EN = 0
    p1_DU = 0
    p1_IT = 0
    p1.append(p1_EN)
    p1.append(p1_DU)
    p1.append(p1_IT)
    p2_EN = 0
    p2_DU = 0
    p2_IT = 0
    p2.append(p2_EN)
    p2.append(p2_DU)
    p2.append(p2_IT)
    for line in instances:
        if line[value] == "TRUE":
            if line[len(line) - 1] == "EN":
                p1_EN += 1
            elif line[len(line) - 1] == "DU":
                p1_DU += 1
            else:
                p1_IT += 1
        elif line[value] == "FALSE":
            if line[len(line) - 1] == "EN":
                p2_EN += 1
            elif line[len(line) - 1] == "DU":
                p2_DU += 1
            else:
                p2_IT += 1
    g1 = p1_EN + p1_DU + p1_IT
    g2 = p2_EN + p2_DU + p2_IT

    if g1 == 0:
        giniInd1 = 1.0
    else:
        giniInd1 = 1 - ((p1_EN/g1)**2 + (p1_DU/g1)**2 + (p1_IT/g1)**2)
    if g2 == 0:
        giniInd2 = 1.0
    else:
        giniInd2 = 1 - ((p2_EN/g2)**2 + (p2_DU/g2)**2 + (p2_IT/g2)**2)
    gini = (g1/(g1+g2) * giniInd1) + (g2/(g1+g2) * giniInd2)
    return gini

def buildDecisionTree(features, instances, featuresSelection, tabSpace, predictorFile):
    majorCount = 0
    majorAttribute = ""
    label1Count = 0
    label2Count = 0
    label3Count = 0
    for line in instances:
        if line[-1] == "EN":
            label1Count += 1
        elif line[-1] == "DU":
            label2Count += 1
        else:
            label3Count += 1
    if label1Count > label2Count and label1Count > label3Count:
        majorCount = label1Count
        majorAttribute = "ENGLISH"
    elif label2Count > label3Count and label2Count > label1Count:
        majorCount = label2Count
        majorAttribute = "DUTCH"
    else:
        majorCount = label3Count
        majorAttribute = "ITALIAN"

    totalTab = '\t' * tabSpace
    tune = 1.0
    if tabSpace == 8 or len(instances) <= 40:
        predictorFile.write(totalTab)
        if majorAttribute == "ENGLISH" and majorAttribute != "DUTCH" and majorAttribute != "ITALIAN":
            result = "ENGLISH"
        elif majorAttribute == "DUTCH" and majorAttribute != "ENGLISH" and majorAttribute != "ITALIAN":
            result = "DUTCH"
        else:
            result = "ITALIAN"
        returnString = 'return \'' + result + '\'\n'
        predictorFile.write(returnString)
        return majorAttribute
    else:
        threshold = 1.0
        for value in range(len(features) - 1):
            impurityRate = calculateImpurity(value, instances)
            if impurityRate <= threshold:
                bestAttribute = value
                threshold = impurityRate
        left = []
        right = []
        for each in instances:
            if each[bestAttribute] != "FALSE":
                left.append(each)
            else:
                right.append(each)
        conditionString = totalTab + "if " + featuresSelection[features[bestAttribute]] + ":\n"
        predictorFile.write(conditionString)
        buildDecisionTree(features, left, featuresSelection, tabSpace + 1, predictorFile)
        predictorFile.write(totalTab)
        predictorFile.write("else:\n")
        buildDecisionTree(features, right, featuresSelection, tabSpace + 1, predictorFile)

def accuracyChecker(engtextDoc, dutextDoc, ittextDoc):
    print("Checking Accuracy")

    files = []
    language = ["English", "Dutch", "Italian"]
    accuracyResult = []
    from predict import classification
    files.append(engtextDoc)
    files.append(dutextDoc)
    files.append(ittextDoc)
    for file in range(len(files)):
        label1Count = 0
        label2Count = 0
        label3Count = 0
        with open(files[file], encoding="UTF-8") as f:
            sentences = f.readlines()
            for line in sentences:
                eachline = line.strip()
                line = line.strip().split()
                result = classification(eachline, line)
                if result == "ENGLISH":
                    label1Count += 1
                elif result == "DUTCH":
                    label2Count += 1
                else:
                    label3Count += 1
            count = []
            count.append(label1Count)
            count.append(label2Count)
            count.append(label3Count)
            total = label1Count + label2Count + label3Count
            accCal = round(count[file] / total * 100, 5)
            accuracyResult.append(accCal)
    for i, l in zip(accuracyResult, language):
        print("Accuracy for " + l + " : " + str(i))

def readingCSVData(trainingDataFile):
    flag = False
    instances = []
    attributes = ""
    with open(trainingDataFile) as data:
        for line in csv.reader(data, delimiter=","):
            if flag == False:
                attributes = line
                flag = True
            else:
                instances.append(line)
        return attributes, instances

def generatePredictor(trainingDataFile):
    print("Reading Training Data and generating predictor program")

    with open("predict.py", "w", encoding="UTF-8") as predictorFile:

        features, instances = readingCSVData(trainingDataFile)
        featuresSelection = {
            features[0]: '"de" in word or "het" in word or "dat" in word or "en" in word or "een" in word or "voor" in word or "van" in word or "welke" in word or "te" in word or "hij" in word or "zij" in word or "op" in word or "ik" in word or "bij" in word',   #DU
            features[1]: '"che" in word or "il" in word or "ll" in word or "e" in word or "un" in word or "di" in word or "per" in word or "era" in word',          #IT
            features[2]: '"the" in word or "but" in word or "for" in word or "which" in word or "that" in word or "and" in word or "not" in word or "to" in word or "in" in word', #EN
            features[3]: '"j" not in inputSentence or "k" not in inputSentence or "w" not in inputSentence or "x" not in inputSentence or "y" not in inputSentence',#IT
            features[4]: '"à" in inputSentence or "è" in inputSentence or "ì" in inputSentence or "ò" in inputSentence or "ù" in inputSentence',                    #IT
            features[5]: '"aa" in inputSentence or "ee" in inputSentence or "ii" in inputSentence or "uu" in inputSentence',                                        #DU
            features[6]: '"ijk" in inputSentence or "sch" in inputSentence or "ijn" in inputSentence',                                                              #DU
            features[7]: '"is" in word or "of" in word or "was" in word or "all" in word',                                                                          #EN/DU
            features[8]: "(\"l'\") in inputSentence or (\"d'\") in inputSentence",                                                                                  #IT
            features[9]: '"come" in word or "a" in word',                                                                                                           #EN/IT
            features[10]: '"si" in word or "le" in word or "ma" in word or "la" in word or "mi" in word or "se" in word',                                           #IT
            features[11]: '"he" in word or "she" in word or "it" in word or "they" in word',                                                                        #EN
            features[12]: 'inputSentence.count("i") >= 11'                                                                                                          #IT
        }
        predictorFile.write(str("""
def classification(inputSentence, word):
"""))
        buildDecisionTree(features, instances, featuresSelection, 1, predictorFile)
        predictorFile.write(str("""
if __name__ == "__main__":
    inputSentence = input("Enter the sentence you want to predict")
    wordArray = inputSentence.split()
    results = classification(inputSentence, wordArray)
    print(results)
"""))

def oneR(language, lc, recordData):
    if language == "ENDU":
        if lc == 0:
            if recordData[0] == "TRUE":
                return "DU"
            else:
                return "EN"
        elif lc == 1:
            if recordData[2] == "TRUE":
                return "EN"
            else:
                return "DU"
        elif lc == 2:
            if recordData[5] == "TRUE":
                return "DU"
            else:
                return "EN"
        elif lc == 3:
            if recordData[6] == "TRUE":
                return "DU"
            else:
                return "EN"
        elif lc == 4:
            if recordData[7] == "TRUE":
                return "EN"
            else:
                return "DU"
        elif lc == 5:
            if recordData[11] == "TRUE":
                return "EN"
            else:
                return "DU"

def adaBoost(language, count, instances):
    recordData = []
    valueENDU = []

    for instance in instances:
        if instance[len(instance) - 1] == "EN" or instance[len(instance) - 1] == "DU":
            recordData.append(instance)

    weight = [1/len(recordData)] * len(recordData)
    for lc in range(count):
        error = 0
        for j in range(len(recordData)):
            if oneR(language, lc, recordData[j]) != recordData[j][len(recordData[j]) - 1]:
                error = error + weight[j]
        for j in range(len(recordData)):
            if oneR(language, lc, recordData[j]) == recordData[j][len(recordData[j]) - 1]:
                weight[j] = weight[j] * (error/(1 - error))
        for j in range(len(recordData)):
            weight[j] /= sum(weight)
        hypothesis_weight = math.log(abs(1 - error) / error, 2)
        valueENDU.append(hypothesis_weight)
    return valueENDU

def adaWriter(valueENDU, adaFile):
    adaFile.write("""
def decisionStump(inputSentence, wordArray):
    valueENDU = """
                + str(valueENDU) +
                """
    
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
""")

def adaBoostAccuracy(engtextDoc, dutextDoc):
    files = []
    language = ["English", "Dutch"]
    accuracyResult = []
    from adaPredict import decisionStump
    files.append(engtextDoc)
    files.append(dutextDoc)
    for file in range(len(files)):
        label1Count = 0
        label2Count = 0
        with open(files[file], encoding="UTF-8") as f:
            sentences = f.readlines()
            for line in sentences:
                eachline = line.strip()
                line = line.strip().split()
                result = decisionStump(eachline, line)
                if result == "ENGLISH":
                    label1Count += 1
                else:
                    label2Count += 1
            count = []
            count.append(label1Count)
            count.append(label2Count)
            total = label1Count + label2Count
            accCal = round(count[file] / total * 100, 5)
            accuracyResult.append(accCal)
    for i, l in zip(accuracyResult, language):
        print("Accuracy for " + l + " : " + str(i))

def startAdaBoost(filename, featureCountENDU):
    print("Starting AdaBoost")

    features, instances = readingCSVData(filename)
    valueENDU = adaBoost("ENDU", featureCountENDU, instances)
    adaFile = open("adaPredict.py", "w", encoding="UTF-8")
    adaWriter(valueENDU, adaFile)
    adaFile.close()
    engtextDoc = input("Enter English language text document filename")
    dutextDoc = input("Enter Dutch language text document filename")
    adaBoostAccuracy(engtextDoc, dutextDoc)


if __name__ == "__main__":
    generatePredictor("data.csv")

    accuracy = int(input("Do you want to check the accuracy 1: Yes  2: No"))
    if accuracy == 1:
        engtextDoc = input("Enter English language text document filename")
        dutextDoc = input("Enter Dutch language text document filename")
        ittextDoc = input("Enter Italian language text document filename")
        accuracyChecker(engtextDoc, dutextDoc, ittextDoc)
    else:
        print("Decision Tree Done")

    adaboost = int(input("Do you want to run AdaBoost   1: Yes    2:No"))
    if adaboost == 1:
        featureCountENDU = 6
        startAdaBoost("data.csv", featureCountENDU)
    else:
        print("Exit")
