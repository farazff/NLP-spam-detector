from copy import deepcopy


def countEveryWord(sentences):
    result = {}
    for sentence in sentences:
        words = str(sentence).split()
        for word in words:
            if not (word in result):
                result[word] = 1
            else:
                result[word] = result[word] + 1
    data_sorted = {k: v for k, v in sorted(result.items(), key=lambda x: x[1])}
    return deepcopy(data_sorted)


def countPairs(sentences):
    result = {}
    for sentence in sentences:
        words = str(sentence).split()
        for i in range(len(words) - 1):
            partOne = words[i]
            partTwo = words[i + 1]
            if partOne in result:
                if partTwo in result[partOne]:
                    result[partOne][partTwo] += 1
                else:
                    result[partOne][partTwo] = 1
            else:
                result[partOne] = {partTwo: 1}
    return deepcopy(result)
