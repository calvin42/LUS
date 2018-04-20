methods = ["absolute", "katz", "kneser_ney", "presmoothed", "unsmoothed", "witten_bell"]

results = {}
for method in methods:
    results[method] = []
    with open(method+"_final_output.txt", "r") as f:
        next_is_the_one = False
        for line in f.readlines():
            if next_is_the_one:
                splitted = line.split("FB1:  ")
                splitted = splitted[1].split("\n")[0]
                results[method].append(splitted)
                next_is_the_one = False
            elif "processed" in line:
                next_is_the_one = True


for key in results.keys():
    print (key, end=";")
print()
for i in range(0, 5):
    for key in results.keys():
        print(results[key][i].replace(".",","), end=";")
    print()
