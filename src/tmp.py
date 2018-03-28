from subprocess import check_output, call, Popen
import math

def prob(word, tag):
    bigram = (word, tag)
    if freq_bigram.get(bigram) is not None:
        return float(freq_bigram[bigram])/float(freq_labels[tag])

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
            
with open("words.txt", "w") as wr:
    wr.writelines("\n".join(words))
with open("tags.txt", "w") as tg:
    tg.writelines("\n".join(tags))

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
    gr.write("0")

with open("unk_graph.txt", "w") as un:
    for tag in tags:
        un.write("0\t0\t<unk>\t"+tag+"\t"+str(float(1/len(tags)))+"\n")
    un.write("0")

call(["ngramsymbols", "words.txt", "words.lex"])
call(["ngramsymbols", "tags.txt", "tags.lex"])
fst = Popen(["fstcompile", "--isymbols=words.lex", "--osymbols=tags.lex", "graph.txt"], stdout=open("train.fst","w"))
unk = Popen(["fstcompile", "--isymbols=words.lex", "--osymbols=tags.lex", "unk_graph.txt"], stdout=open("unk.fst","w"))
# union = Popen(["fstcompose", "train.fst", "unk.fst"], stdout=open("complete_train.fst", "w"))

