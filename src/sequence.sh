#!/bin/bash
ngramsymbols words.txt words.lex
# ngramsymbols tags.txt tags.lex

./compile_far.sh

./language_modeling.sh words
# ./language_modeling.sh tags

fstcompile --isymbols=words.lex --osymbols=words.lex graph.txt > train.fst


# fstdraw --isymbols=words.lex --osymbols=tags.lex train.fst | dot -Teps > prova.eps
# open prova.eps

./execute.sh absolute
./execute.sh katz
./execute.sh kneser_ney
./execute.sh presmoothed
./execute.sh unsmoothed
./execute.sh witten_bell
mkdir predicted
mv output-*.txt predicted
python3 eval.py
mkdir evaluations
mv eval_output*.txt evaluations
./eval.sh