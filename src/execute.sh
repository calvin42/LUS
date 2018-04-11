#!/bin/bash

# filename="../P1_Data/data/NLSPARQL.test.data"

method=$1
filename="./test_modified.txt"
for i in `seq 1 5`;
do
    echo "$i"
    while read line
    do
        # echo "$line"
        echo $line | farcompilestrings --symbols=words.lex --unknown_symbol='<unk>' --generate_keys=1 --keep_symbols | farextract --filename_prefix="$i-$method-" --filename_suffix='.fst'
        fstcompose $i-$method-1.fst train.fst | fstcompose - lm/$i-$method.lm | fstrmepsilon | fstshortestpath | fsttopsort | fstprint --isymbols=words.lex --osymbols=words.lex >> "output-$i-$method.txt"
    done < $filename
done

# echo "INIZIO"
# i=1
# while read line
# do
#     # echo "$line"
#     echo $line | farcompilestrings --symbols=words.lex --unknown_symbol='<unk>' --generate_keys=1 --keep_symbols | farextract --filename_prefix="$i-$method-" --filename_suffix='.fst'
#     fstcompose $i-$method-1.fst train.fst | fstcompose - lm/$i-$method.lm | fstrmepsilon | fstshortestpath | fsttopsort | fstprint --isymbols=words.lex --osymbols=words.lex >> "output-$i-$method.txt"
# done < $filename

# echo "FINE"