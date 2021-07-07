def P_unigram(word, M, dictData):
    return dictData[word] / M


def P_bigram(wordi, wordi_1, dictData2D, dictData):
    return dictData2D[wordi][wordi_1] / dictData[wordi_1]


def P_bigramNormal(wordi, wordi_1, dictData2D, dictData, M):
    landa1 = 0.25
    landa2 = 0.25
    landa3 = 0.5
    epsilon = 0.5
    return landa3 * P_bigram(wordi, wordi_1, dictData2D, dictData) + \
           landa2 * P_unigram(wordi, M, dictData) + \
           landa1 * epsilon


def P_WL(comment, dictData, dictData2D, M):
    words = comment.split(" ")
    possibility = P_unigram(words[0])
    for i in range(1, len(words)):
        possibility *= P_bigramNormal(words[i], words[i - 1], dictData2D, dictData, M)
    return possibility
