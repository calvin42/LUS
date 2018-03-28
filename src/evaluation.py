# data = []
# with open("sample.txt", "r") as sp:
#     data = sp.readlines()
#                  ref
#               1       0        
#   hyp   1     TP      FP
#         0     FN      TN

class Eval:
    def __init__(self, data):
        self.__data = data
        self.__tp = ("1", "1")
        self.__fp = ("1", "0")
        self.__fn = ("0", "1")
        self.__tn = ("0", "0")
        self.__results = {
                self.__tp: 0,
                self.__fp: 0,
                self.__fn: 0,
                self.__tn: 0
            }
        self.__accuracy = 0
        self.__f1 = 0
        self.__recall = 0
        self.__precision = 0

        for line in self.__data:
            hyp = line.split("\t")[0]
            ref = line.split("\t")[1].split("\n")[0]
            self.__results[(hyp, ref)] += 1
    # end __init__


# ACCURACY
# TP + TN / TP + TN + FP + FN
    def accuracy(self):    
        self.__accuracy = float(self.__results[self.__tp] + self.__results[self.__tn]) / float(self.__results[self.__tp] + self.__results[self.__tn] + self.__results[self.__fp] + self.__results[self.__fn])
        print ("Accuracy: "+str(self.__accuracy))
        return self.__accuracy

# PRECISION
# TP / TP + FP
    def precision(self):
        self.__precision = float(self.__results[self.__tp])/float(self.__results[self.__tp] + self.__results[self.__fp])
        print ("Precision: "+str(self.__precision))
        return self.__precision

# RECALL
# TP / TP + FN
    def recall(self):
        self.__recall = float(self.__results[self.__tp])/ float(self.__results[self.__tp] + self.__results[self.__fn])
        print ("Recall: "+str(self.__recall))
        return self.__recall

# F1
# 2 * Precision * recall / precision + recall
    def f1(self):
        self.__f1 = 2 * float(self.__precision) * float(self.__recall) / float(self.__precision) + float(self.__recall)
        print ("F1: "+str(self.__f1))
        return self.__f1