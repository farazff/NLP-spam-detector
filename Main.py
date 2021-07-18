from Learn import countEveryWord, countPairs
from Possibilities import P_WL
import Possibilities
from Preprocessor import DatasetsPreprocessor
import random


def tester(goodSentencesTst, badSentencesTst):
    goodCount, goodPairs = countEveryWord(goodSentencesTst), countPairs(goodSentencesTst)
    badCount, badPairs = countEveryWord(badSentencesTst), countPairs(badSentencesTst)
    truePredictGood, truePredictBad, falsePredictBad, falsePredictGood = 0.0, 0.0, 0.0, 0.0

    goodM = 0
    for word in goodCount:
        goodM = goodM + goodCount[word]

    badM = 0
    for word in badCount:
        badM = badM + badCount[word]

    for comment in goodSentencesTst:
        PGood, PBad = P_WL(comment, goodCount, goodPairs, goodM), P_WL(comment, badCount, badPairs, badM)
        if PGood > PBad:
            truePredictGood += 1
        else:
            falsePredictGood += 1

    for comment in badSentencesTst:
        PGood, PBad = P_WL(comment, goodCount, goodPairs, goodM), P_WL(comment, badCount, badPairs, badM)
        if PGood < PBad:
            truePredictBad += 1
        else:
            falsePredictBad += 1

    precision = truePredictGood / (truePredictGood + falsePredictGood)
    recall = truePredictGood / (truePredictGood + falsePredictBad)
    F1_Score = (2 * precision * recall) / (precision + recall)

    print("\nTRUE  Predict Good   => ", 100 * truePredictGood / (truePredictGood + falsePredictGood), "%",
          "\nFALSE Predict Good   => ", 100 * falsePredictGood / (truePredictGood + falsePredictGood), "%",
          "\nTRUE  Predict Bad    => ", 100 * truePredictBad / (truePredictBad + falsePredictBad), "%",
          "\nFALSE Predict Bad    => ", 100 * falsePredictBad / (truePredictBad + falsePredictBad), "%",
          "\n--------------------------------------------")
    print("Precision            => ", precision,
          "\nRecall               => ", recall,
          "\nF1_Score             => ", F1_Score,
          "\n--------------------------------------------\nEnter comment >>")

    return precision


def bestParametersSearcher(goodSentencesTst, badSentencesTst):
    bestPrecision = 0
    bestParameters = None
    for i in range(100):
        parameters = randomAdmissibleParameterGenerator()
        Possibilities.lambda1 = parameters[0]
        Possibilities.lambda2 = parameters[1]
        Possibilities.lambda3 = parameters[2]
        Possibilities.epsilon = parameters[3]
        precision = tester(goodSentencesTst, badSentencesTst)
        if precision > bestPrecision:
            bestParameters = parameters
            bestPrecision = precision

    print("Best Precision   =>", bestPrecision)
    print("\u03BB1 =", bestParameters[0], " , ",
          "\u03BB2 =", bestParameters[1], " , ",
          "\u03BB3 =", bestParameters[2], " , ",
          "\u03F5 =", bestParameters[3])


def randomAdmissibleParameterGenerator():
    while True:
        lambda1 = random.uniform(0, 1)
        lambda2 = random.uniform(0, 1)
        lambda3 = 1 - lambda1 - lambda2
        if lambda3 > 0:
            epsilon = random.uniform(0, 1)
            return lambda1, lambda2, lambda3, epsilon


def main():
    goodSentences = DatasetsPreprocessor()[0]
    badSentences = DatasetsPreprocessor()[1]
    goodSentencesTst = DatasetsPreprocessor()[2]
    badSentencesTst = DatasetsPreprocessor()[3]
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
    tester(goodSentencesTst, badSentencesTst)

    # uncomment line below  to find best parameters value
    # bestParametersSearcher(goodSentencesTst, badSentencesTst)

    while True:
        comment = input()
        if comment == "!q":
            break
        PGood = P_WL(comment, goodCount, goodPairs, goodM)
        PBad = P_WL(comment, badCount, badPairs, badM)

        print(PGood, " ", PBad)

        if PGood > PBad:
            print("Good so NOT FILTER THIS")
        else:
            print("Bad so FILTER THIS")


if __name__ == "__main__":
    main()
