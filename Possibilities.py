def P_unigram(word, M, dictData):
    if word in dictData:
        return dictData[word] / M
    return 0.01


def P_bigram(secondWord, firstWord, dictData2D, dictData):
    countFirstWord = 0
    if firstWord in dictData:
        countFirstWord = dictData[firstWord]

    countPair = 0
    if firstWord in dictData2D:
        if secondWord in dictData2D[firstWord]:
            countPair = dictData2D[firstWord][secondWord]

    if countPair == 0:
        return 0
    return countPair / countFirstWord


def P_bigramNormal(secondWord, firstWord, dictData2D, dictData, M):
    lambda1 = 0.10
    lambda2 = 0.15
    lambda3 = 0.75
    epsilon = 0.1
    return lambda3 * P_bigram(secondWord, firstWord, dictData2D, dictData) + \
           lambda2 * P_unigram(secondWord, M, dictData) + lambda1 * epsilon


def P_WL(comment, dictData, dictData2D, M):
    words = comment.split(" ")
    possibility = P_unigram(words[0], M, dictData)
    for i in range(1, len(words)):
        possibility *= P_bigramNormal(words[i], words[i - 1], dictData2D, dictData, M)
    return possibility
