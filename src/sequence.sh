#!/bin/bash
ngramsymbols words.txt words.lex
# ngramsymbols tags.txt tags.lex

# ./compile_far.sh
farcompilestrings --symbols=words.lex --unknown_symbol='<unk>' iob-phrases.txt > lm/words.far

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

mkdir fsts
mv *-1.fst fsts
mkdir predicted
mv output-*.txt predicted
python3 eval.py
mkdir evaluations
mv eval_output*.txt evaluations

./eval.sh absolute > absolute_final_output.txt
./eval.sh katz > katz_final_output.txt
./eval.sh kneser_ney > kneser_ney_final_output.txt
./eval.sh presmoothed > presmoothed_final_output.txt
./eval.sh unsmoothed >unsmoothed _final_output.txt
./eval.sh witten_bell > witten_bell_final_output.txt
mkdir output
mv *final_output.txt output