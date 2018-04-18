#!/bin/bash

# filename="../P1_Data/data/NLSPARQL.test.data"

method=$1
from=$2
to=$3
filename="./test_modified.txt"

echo "$method"
for i in `seq $from $to`;
do
    k=0
    echo "$i"
    while read line
    do
        # echo "$line"
        if [ $((k%100)) -eq 0 ]
        then
            echo "$k"
        fi
        echo $line | farcompilestrings --symbols=words.lex --unknown_symbol='<unk>' --generate_keys=1 --keep_symbols | farextract --filename_prefix="$i-$method-" --filename_suffix='.fst'
        fstcompose $i-$method-1.fst train.fst | fstcompose - lm/$i-$method.lm | fstrmepsilon | fstshortestpath | fsttopsort | fstprint --isymbols=words.lex --osymbols=words.lex >> "output-$i-$method.txt"
        k=$((k+1))
    done < $filename
done

# echo "INIZIO"
# i=2
# k=0
# while read line
# do
#     if [ $((k%100)) -eq 0 ]
#     then
#         echo "$k"
#     fi
#     echo $line | farcompilestrings --symbols=words.lex --unknown_symbol='<unk>' --generate_keys=1 --keep_symbols | farextract --filename_prefix="$i-$method-" --filename_suffix='.fst'
#     fstcompose $i-$method-1.fst train.fst | fstcompose - lm/$i-$method.lm | fstrmepsilon | fstshortestpath | fsttopsort | fstprint --isymbols=words.lex --osymbols=words.lex >> "output-$i-$method.txt"
#     k=$((k+1))
# done < $filename

# echo "FINE"