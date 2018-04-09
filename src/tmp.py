from subprocess import check_output, call, Popen
import math
from collections import Counter

def prob(word, tag):
    bigram = (word, tag)
    if freq_bigram.get(bigram) is not None:
        return float(freq_bigram[bigram])/float(freq_labels[tag])

def read_data():
    with open("../P1_data/data/NLSPARQL.train.data", "r") as tr:
        for line in tr.readlines():
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

def words_lexicon():            
    with open("words.txt", "w") as wr:
        wr.writelines("\n".join(words))

def tags_lexicon():
    with open("tags.txt", "w") as tg:
        tg.writelines("\n".join(tags))

def graph():
    with open("graph.txt", "w") as gr:
        i = 0
        done = []
        while i < len(words):
            if ((words[i], tags[i]) not in done): 
                done.append((words[i], tags[i]))
                p = prob(words[i], tags[i])
                w = -math.log(p)
                gr.write("0\t0\t"+words[i].split("\n")[0]+"\t"+tags[i]+"\t"+str(w)+"\n")
            i += 1
        for tag in tags:
            if (tag) not in done:
                gr.write("0\t0\t<unk>\t"+tag+"\t"+str(float(1/len(tags)))+"\n")
                done.append(tag)
        gr.write("0")


def init():
    read_data()
    words_lexicon()
    tags_lexicon()
    graph()


###################################################
###################################################
###################################################
###################################################

words = []
tags = []
freq_bigram = {}
freq_labels = {}

###################################################
###################################################
###################################################
###################################################

init()

Popen(["./sequence.sh"])