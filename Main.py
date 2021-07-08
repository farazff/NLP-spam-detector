from Learn import countEveryWord, countPairs
from Possibilities import P_WL
from Preprocessor import DatasetsPreprocessor


def main():
    goodSentences = DatasetsPreprocessor()[0]
    badSentences = DatasetsPreprocessor()[1]
    goodCount = countEveryWord(goodSentences)
    goodPairs = countPairs(goodSentences)
    badCount = countEveryWord(badSentences)
    badPairs = countPairs(badSentences)

    goodM = 0
    for word in goodCount:
        goodM = goodM + goodCount[word]

    badM = 0
    for word in badCount:
        badM = badM + badCount[word]

    while True:
        comment = input()
        if comment == "!q":
            break
        PGood = P_WL(comment, goodCount, goodPairs, goodM)
        PBad = P_WL(comment, badCount, badPairs, badM)

        print(PGood, " ", PBad)

        if PGood > PBad:
            print("Good")
        else:
            print("Bad")


if __name__ == "__main__":
    main()
