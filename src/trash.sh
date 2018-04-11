# echo 'star of thor' | farcompilestrings --symbols=words.lex --unknown_symbol='<unk>' --generate_keys=1 --keep_symbols | farextract --filename_suffix='.fst'

# fstcompose 1.fst train.fst > out.fst
# fstdraw --isymbols=words.lex --osymbols=tags.lex out.fst | dot -Teps > prova.eps
# open prova.eps
# fstshortestpath out.fst | fstrmepsilon | fsttopsort | fstprint --isymbols=words.lex --osymbols=tags.lex > provetta.txt
# fstcompose 1.fsa train.fst | fstcompose - $i-$method.lm | fstrmepsilon | fstshortestpath

# len=`wc -l $filename | cut -d ' ' -f 1`



    # fstcompose 1.fst train.fst > out.fst
#     fstshortestpath out.fst | fstrmepsilon |  | fstprint --isymbols=words.lex --osymbols=tags.lex >> "output.txt"
# done
