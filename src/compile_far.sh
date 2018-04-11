#!/bin/bash

farcompilestrings --symbols=words.lex --unknown_symbol='<unk>' iob-phrases.txt > lm/words.far
# farcompilestrings --symbols=tags.lex --unknown_symbol='<unk>' tags.txt > lm/tags.far