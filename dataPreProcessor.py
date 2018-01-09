import re
import csv

def mergeFile():
    file1 = "Training_EN.txt"
    file2 = "Training_DU.txt"
    file3 = "Training_IT.txt"
    files = []
    fline = []
    lineData = []
    dataArray = []
    files.append(file1)
    files.append(file2)
    files.append(file3)
    filename = "TrainingData.txt"
    with open(filename, "w") as file:
        for each in files:
            with open(each, "r") as rf:
                readText = rf.readlines()
                for line in readText:
                    file.write(line)

    with open(filename, "r") as file:
        fileLines = file.readlines()
        for line in fileLines:
            line = line.strip().split(", ")
            for each in line:
                each = each.upper()
            lineData.append(line)

    with open('data.csv', 'w', newline='') as data:
        writer = csv.writer(data)
        writer.writerows([['COLUMN1', 'COLUMN2', 'COLUMN3', 'COLUMN4', 'COLUMN5', 'COLUMN6', 'COLUMN7',
                           'COLUMN8', 'COLUMN9', 'COLUMN10', 'COLUMN11', 'COLUMN12', 'COLUMN13', 'Label']])
        writer.writerows(lineData)

    print("Training Data merged and CSV created")

def writeTrainingData(featureVector, contentType):
    print("Generating Training Data file")

    feature = ""
    count = 0
    filename = "Training_" + contentType + ".txt"
    with open(filename, "w") as file:
        for sample in featureVector:
            if count <= 4000:
                for each in sample:
                    for i in each:
                        if str(i) == "EN" or str(i) == "DU" or str(i) == "IT":
                            i = i + "\n"
                        feature += str(i) + ", "
                feature = feature.strip(", ")
                file.write(feature)
                feature = ""
                count += 1

def featureSelection(train, trainingData, contentType):
    print("Feature Selection")

    featureVector = []
    sampleVector = []

    for sentence in trainingData:

        notJXY = "FALSE"              # not contains letter j, k, w, x, y	Italian
        spcItalianChar = "FALSE"      # Special char in Italian
        twoVowels = "FALSE"           # two vowels in row					Dutch
        substringDutch = "FALSE"        # Substring "sch"        			Dutch
        containsISWAS = "FALSE"          # if contains "is"					English/ Dutch
        substringLastrp = "FALSE"     # word containing l'				Italian
        containsCOME = "FALSE"        #English/Italian
        englishWords = "FALSE"
        dutchWords = "FALSE"
        italianWords = "FALSE"        #che    il  e
        itaCommon = "FALSE"
        engCommon = "FALSE"
        countI = "FALSE"
        count = 0

        for word in sentence:

            if re.match('[0-9]*', word):
                word = re.sub('[0-9]*', '', word)

            if re.match('[!?~`@#$%&)(_=+/.,"»;«-]', word):
                word = re.sub('[!?~`@#$%&)(_=+/.,"»;«-]', '', word)

            word = word.lower()
            if "de" == word or "het" == word or "dat" == word or "en" == word or "een" == word or "voor" == word or "van" == word or "welke" == word \
                    or "te" == word or "hij" == word or "zij" == word or "op" == word or "ik" == word or "bij" == word:
                dutchWords = "TRUE"
            if "che" == word or "il" == word or "ll" == word or "e" == word or "un" == word or "di" == word or "per" == word or "era" == word:
                italianWords = "TRUE"
            if "the" == word or "but" == word or "for" == word or "which" == word or "that" == word or "and" == word or "not" == word \
                    or "to" == word or "in" == word:
                englishWords = "TRUE"
            if "j" not in word or "k" not in word or "w" not in word or "x" not in word or "y" not in word:
                notJXY = "TRUE"
            if "à" in word or "è" in word or "ì" in word or "ò" in word or "ù" in word:
                spcItalianChar = "TRUE"
            if "aa" in word or "ee" in word or "ii" in word or "uu" in word:
                twoVowels = "TRUE"
            if "ijk" in word or "sch" in word or "ijn" in word:
                substringDutch = "TRUE"
            if "is" == word or "of" == word or "was" == word or "all" in word:
                containsISWAS = "TRUE"
            if "l'" in word or "d'" in word:
                substringLastrp = "TRUE"
            if "come" == word or "a" == word:
                containsCOME = "TRUE"
            if "si" == word or "le" == word or "ma" == word or "la" == word or "mi" == word or "se" == word:
                itaCommon = "TRUE"
            if "he" == word or "she" == word or "it" == word or "they" == word:
                engCommon = "TRUE"
            numI = word.count("i")
            count += numI
            numI = 0
        if count >= 11:
            countI = "TRUE"

        sampleVector.append([dutchWords, italianWords, englishWords, notJXY, spcItalianChar,
                             twoVowels, substringDutch, containsISWAS, substringLastrp,
                             containsCOME, itaCommon, engCommon, countI, contentType])

        featureVector.append(sampleVector)
        sampleVector = []
    writeTrainingData(featureVector, contentType)

def createTrainingData(text, contentType):
    print("Data Preprocessing")
    sentence = ""
    trainingData = []
    trainingWords = []
    train = []
    sample = []
    count = 15
    for line in text:
        line = line.split(" ")
        for word in line:
            if word != "":
                trainingWords.append(word)
    for word in trainingWords:
        if len(sample) < count-1:
            sample.append(word)
        else:
            sample.append(word)
            trainingData.append(sample)
            sample = []
    for sample in trainingData:
        sentence = " ".join(word for word in sample)
        sentence = sentence.strip()
        train.append([sentence, contentType])
    featureSelection(train, trainingData, contentType)

def readFile(filename, contentType):
    print("Reading TextFile", filename)
    text = []
    with open(filename, encoding="utf8") as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        text.append(line)
    createTrainingData(text, contentType)

if __name__ == '__main__':
    merge = int(input("Merge Training Data file 1: Yes 2: No"))
    if merge == 1:
        mergeFile()
    else:
        filename = input("Enter the filename to read:")
        fileType = int(input("Select the language for given filename    1: English 2: Dutch 3: Italian"))
        if fileType == 1:
            contentType = "EN"
        elif fileType == 2:
            contentType = "DU"
        elif fileType == 3:
            contentType = "IT"
        else:
            print("Fail to recognize the language")

        if contentType != None:
            readFile(filename, contentType)
        else:
            print("Exit")