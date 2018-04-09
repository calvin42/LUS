#!/bin/bash

farcompilestrings --symbols=words.lex --unknown_symbol='<unk>' words.txt > lm/words.far
farcompilestrings --symbols=tags.lex --unknown_symbol='<unk>' tags.txt > lm/tags.far