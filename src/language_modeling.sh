#!/bin/bash
# FAR=$1
# 

FAR=$1
from=$2
to=$3
METHODS=("absolute" "katz" "kneser_ney" "presmoothed" "unsmoothed" "witten_bell") # "katz_frac")


for i in `seq $from $to`;
do
    CNTS="./lm/$FAR-$i.cnts"
    ngramcount --order=$i --require_symbols=false "./lm/$FAR.far" > $CNTS
    for METHOD in "${METHODS[@]}"
    do
        # echo "$METHOD"
        ngrammake --method=$METHOD $CNTS > ./lm/$i-$METHOD.lm
    done
done

# rm lm/*.far
# rm lm/*.cnts
