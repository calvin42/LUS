tags = []
with open("../P1_Data/data/NLSPARQL.test.data", "r") as ts:
    for line in ts.readlines():
        if line != "\n":
            tags.append(line.split("\t")[1].split("\n")[0])

methods = ["absolute", "katz", "kneser_ney", "presmoothed", "unsmoothed", "witten_bell"]
print(len(tags))

for method in methods:
    for i in range(1, 6):
        k = 0
        output = []
        filename = "output-"+str(i)+"-"+method+".txt"
        with open(filename, "r") as f:
            for line in f.readlines():
                if k < len(tags):
                    if len(line.split("\t")) > 2:
                        start, end, word, pos, wgt  = line.split("\t")
                        output.append(word + " " + tags[k] + " " + pos)
                        k += 1
        with open("eval_output_"+str(i)+"-"+method+".txt", "w") as ev:
            for line in output:
                ev.write(line+"\n")