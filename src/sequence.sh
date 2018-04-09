#!/bin/bash
ngramsymbols words.txt words.lex
ngramsymbols tags.txt tags.lex

./compile_far.sh

./language_modeling.sh words
# ./language_modeling.sh tags

fstcompile --isymbols=words.lex --osymbols=tags.lex graph.txt > train.fst


# fstdraw --isymbols=words.lex --osymbols=tags.lex train.fst | dot -Teps > prova.eps
# open prova.eps


# echo 'star of thor' | farcompilestrings --symbols=words.lex --unknown_symbol='<unk>' --generate_keys=1 --keep_symbols | farextract --filename_suffix='.fst'

# fstcompose 1.fst train.fst > out.fst
# fstdraw --isymbols=words.lex --osymbols=tags.lex out.fst | dot -Teps > prova.eps
# open prova.eps
# fstshortestpath out.fst | fstrmepsilon | fsttopsort | fstprint --isymbols=words.lex --osymbols=tags.lex > provetta.txt
# fstcompose 1.fsa train.fst | fstcompose - pos.lm | fstrmepsilon | fstshortestpath
filename="../P1_Data/data/NLSPARQL.test.data"
# len=`wc -l $filename | cut -d ' ' -f 1`

# while read line
# do
#     echo "Executing line:"
#     echo "$line"
#     word=$(echo $line | cut -f 1)
#     tag=$(echo $line | cut -f 2)
#     echo $word | farcompilestrings --symbols=words.lex --unknown_symbol='<unk>' --generate_keys=1 --keep_symbols | farextract --filename_suffix='.fst'
#     fstcompose 1.fst train.fst > out.fst
#     fstshortestpath out.fst | fstrmepsilon | fsttopsort | fstprint --isymbols=words.lex --osymbols=tags.lex >> "output.txt"
# done < $filename