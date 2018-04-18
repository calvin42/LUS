#!/bin/bash
mkdir lm
mkdir fsts
mkdir predicted
mkdir evaluations
mkdir output

ngramsymbols words.txt words.lex
# ngramsymbols tags.txt tags.lex

# ./compile_far.sh
farcompilestrings --symbols=words.lex --unknown_symbol='<unk>' iob-phrases.txt > lm/words.far

./language_modeling.sh words 1 9
# ./language_modeling.sh tags

fstcompile --isymbols=words.lex --osymbols=words.lex graph.txt > train.fst


# fstdraw --isymbols=words.lex --osymbols=tags.lex train.fst | dot -Teps > prova.eps
# open prova.eps

./execute.sh absolute 1 9
./execute.sh katz 1 9
./execute.sh kneser_ney 1 9
./execute.sh presmoothed 1 9
./execute.sh unsmoothed 1 9
./execute.sh witten_bell 1 9


mv *-1.fst fsts
mv output-*.txt predicted
python3 eval.py
mv eval_output*.txt evaluations

./eval.sh absolute > absolute_final_output.txt
./eval.sh katz > katz_final_output.txt
./eval.sh kneser_ney > kneser_ney_final_output.txt
./eval.sh presmoothed > presmoothed_final_output.txt
./eval.sh unsmoothed >unsmoothed_final_output.txt
./eval.sh witten_bell > witten_bell_final_output.txt
mv *final_output.txt output