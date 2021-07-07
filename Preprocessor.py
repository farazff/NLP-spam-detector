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
                                       .replace("[", "") \
                                       .replace("]", "") \
                                       .replace("(", "") \
                                       .replace(")", "") \
                                       .replace(":", "") \
                                       .replace(";", "") \
                                       .replace("  ", " ") \
                                       .replace("   ", " ") \
                                       .replace(" \n", "") \
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
                                          .replace("(", "") \
                                          .replace(")", "") \
                                          .replace(":", "") \
                                          .replace(";", "") \
                                          .replace("  ", " ") \
                                          .replace("   ", " ") \
                                          .replace(" \n", "") \
                                          .replace("\n", ""))
    return OkComments_PreProcessed, NotOkComments_PreProcessed

