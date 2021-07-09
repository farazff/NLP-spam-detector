import random
def DatasetsPreprocessor():
    OkComments_Dataset = "Datasets/rt-polarity.pos"
    NotOkComments_Dataset = "Datasets/rt-polarity.neg"
    OkComments_PreProcessed = []
    NotOkComments_PreProcessed = []
    file = open(OkComments_Dataset, 'r')
    for line in file.readlines():
        OkComments_PreProcessed.append(line.replace(".", "") \
                                       .replace(",", "") \
                                       .replace("-", "") \
                                       .replace("'", "") \
                                       .replace("\"", "") \
                                       .replace("/", "") \
                                       .replace("?", "") \
                                       .replace("ing", "") \
                                       .replace("[", "") \
                                       .replace("]", "") \
                                       .replace("(", "") \
                                       .replace(")", "") \
                                       .replace(":", "") \
                                       .replace(";", "") \
                                       .replace("  ", " ") \
                                       .replace("   ", " ") \
                                       .replace("\n", ""))
    file = open(NotOkComments_Dataset, 'r')
    for line in file.readlines():
        NotOkComments_PreProcessed.append(line.replace(".", "") \
                                          .replace(",", "") \
                                          .replace("-", "") \
                                          .replace("'", "") \
                                          .replace("\"", "") \
                                          .replace("/", "") \
                                          .replace("?", "") \
                                          .replace("[", "") \
                                          .replace("]", "") \
                                          .replace("ing", "") \
                                          .replace("(", "") \
                                          .replace(")", "") \
                                          .replace(":", "") \
                                          .replace(";", "") \
                                          .replace("  ", " ") \
                                          .replace("   ", " ") \
                                          .replace(" \n", "") \
                                          .replace("\n", ""))
    random.shuffle(OkComments_PreProcessed)
    random.shuffle(NotOkComments_PreProcessed)

    return OkComments_PreProcessed[int(0.1*len(OkComments_PreProcessed)):],\
           NotOkComments_PreProcessed[int(0.1*len(NotOkComments_PreProcessed)):], \
           OkComments_PreProcessed[0:int(0.1 * len(OkComments_PreProcessed))], \
           NotOkComments_PreProcessed[0:int(0.1 * len(NotOkComments_PreProcessed))]
