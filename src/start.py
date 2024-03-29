from subprocess import check_output, call, Popen
from collections import Counter
import math
import sys


def prob(word, tag):
    bigram = (word, tag)
    if freq_bigram.get(bigram) is not None:
        return float(freq_bigram[bigram])/float(freq_labels[tag])


def transform(word, tag):
    tmp = tag.split("-")[0]
    return tmp+"-"+word

def prepare_o_data():
    with open("../P1_data/data/NLSPARQL.train.data", "r") as tr:
        with open("../P1_data/data/NLSPARQL.train.o.data.txt", "w") as o:
            for line in tr.readlines():
                if line == "\n":
                    o.write("\n")
                splitted = line.split("\t")
                if len(splitted) > 1:
                    splitted[1] = splitted[1].split("\n")[0]
                    if (splitted[1] == "O"):
                        o.write(splitted[0]+"\t"+transform(splitted[0], splitted[1])+"\n")
                    else:
                        o.write(splitted[0]+"\t"+splitted[1]+"\n")


def read_data(filename):
    phrases = []
    sentence = ""
    with open(filename, "r") as tr:
        for line in tr.readlines():
            if line == "\n":
                # print(sentence)
                phrases.append(sentence)
                sentence = ""
            else:
                # print(line.split("\t")[1].split("\n")[0])
                sentence = sentence+" "+line.split("\t")[1].split("\n")[0]
                # print (sentence)
            splitted = line.split("\t")
            if len(splitted) > 1:
                splitted[1] = splitted[1].split("\n")[0]
                words.append(splitted[0])
                tags.append(splitted[1])
                if freq_bigram.get((splitted[0], splitted[1])) is None:
                    freq_bigram[(splitted[0], splitted[1])] = 1
                else:
                    freq_bigram[(splitted[0], splitted[1])] += 1
                if freq_labels.get(splitted[1]) is None:
                    freq_labels[splitted[1]] = 1
                else:
                    freq_labels[splitted[1]] += 1

    with open("frequence_bigram.txt", "w") as fr:
        for bigram in freq_bigram:
            fr.write(str(bigram)+": "+str(freq_bigram[bigram])+"\n")
    with open("frequence_label.txt", "w") as fr:
        for lab in freq_labels:
            fr.write(lab+": "+str(freq_labels[lab])+"\n")
    with open("frequence_unigram", "w") as fr:
        cnt = Counter(words)
        for el in cnt:
            fr.write(el+ ": "+str(cnt[el])+"\n")
    with open("iob-phrases.txt", "w") as iob:
        # print (phrases)
        for sentence in phrases:
            iob.write(sentence+"\n")
    # with open("tags-only.txt", "w") as tg:
    #     for tag in o_tags:
    #         tg.write()
    

def words_lexicon():            
    with open("words.txt", "w") as wr:
        wr.writelines("\n".join(words))
        wr.write("\n")
        wr.writelines("\n".join(tags))

def graph():
    with open("graph.txt", "w") as gr:
        i = 0
        done = []
        while i < len(words):
            if ((words[i], tags[i]) not in done): 
                done.append((words[i], tags[i]))
                p = prob(words[i], tags[i])
                print (words[i], tags[i], p)
                w = -math.log(p)
                # print(str(w))
                gr.write("0\t0\t"+words[i].split("\n")[0]+"\t"+tags[i]+"\t"+str(w)+"\n")
            i += 1
        for tag in tags:
            if (tag) not in done:
                gr.write("0\t0\t<unk>\t"+tag+"\t"+str(float(1/len(tags)))+"\n")
                done.append(tag)
        gr.write("0")


def divide_test():
    phrases = []
    sentence = ""
    with open("../P1_Data/data/NLSPARQL.test.data", "r") as ts:
        for line in ts.readlines():
            if line == "\n":
                phrases.append(sentence)
                sentence = ""
            else:
                word, tag = line.split("\t")
                sentence = sentence + ' ' + word

    with open("test_modified.txt", "w") as t:
        for phrase in phrases:
            t.write(phrase+"\n")




def init(filename):
    prepare_o_data()
    read_data(filename)
    words_lexicon()
    graph()
    divide_test()


###################################################
###################################################
###################################################
###################################################

words = []
tags = []
o_tags = []
freq_bigram = {}
freq_labels = {}
filename = sys.argv[1]
###################################################
###################################################
###################################################
###################################################

init(filename)

Popen(["./sequence.sh"])