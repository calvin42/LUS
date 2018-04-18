def transform(word, tag):
    tmp = tag.split("-")[0]
    return tmp+"-"+word

tags = []
with open("../P1_Data/data/NLSPARQL.test.data", "r") as ts:
    for line in ts.readlines():
        if line != "\n":
            tmp = line.split("\t")
            tag = tmp[1].split("\n")[0]
            # word = tmp[0]
            # new_tag = transform(word, tag)
            # if new_tag not in tags:
            tags.append(tag)


methods = ["absolute", "katz", "kneser_ney", "presmoothed", "unsmoothed", "witten_bell"]
# methods = ["presmoothed", "unsmoothed", "witten_bell"]

# print(len(tags))

for method in methods:
    for i in range(1, 6):
        k = 0
        output = []
        filename = "predicted/output-"+str(i)+"-"+method+".txt"
        with open(filename, "r") as f:
            for line in f.readlines():
                if k < len(tags):
                    if len(line.split("\t")) > 2:
                        splitted = line.split("\t")
                        word = splitted[2]
                        pos = splitted[3]
                        if "O-" in pos:
                            pos = pos.split("-")[0]
                        output.append(word + " " + tags[k] + " " + pos)
                        k += 1
        with open("eval_output_"+str(i)+"-"+method+".txt", "w") as ev:
            for line in output:
                ev.write(line+"\n")
