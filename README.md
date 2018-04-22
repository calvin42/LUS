# Language Understanding Systems --- Mid-Term project: FST & GRM Tools for SLU

## Requirements
This project requires th installation of:
1. [OpenGRM](http://www.opengrm.org/twiki/bin/view/GRM/WebHome) and [OpenFST](http://www.openfst.org/twiki/bin/view/FST/WebHome) for command line.
2. Python3

## Execution
Go to folder named "src" and execute
```./satart.sh```
## Scripts
### start.sh
It's the script that calls start.py passing the starting dataset as parameter. The first time with the original dataset, the second time with the modified dataset for the "O tags".
### start.py
It elaborates the dataset creating:
1. the frequency of tokens and frequency of bigrams token-tag files;
2. words.txt that will be the input for the creation of the lexicon;
3. the testset with the whole sentence in one line;
4. the IOB-sentences file;
5. the modified version of the initial dataset with the O tags.
At the end it calls sequence.sh
### sequence.sh
This script creates all the necessery directories, the lexicon, the FAR file, the language models, train.fst and it calls execute.sh with many different parameters.
Then it call eval.py and move every file in the relative directory. It calls eval.sh and move all the results into the folder called "output".
### language_modeling.sh
It creates every language model using ngrammake.
### execute.sh
It's the script that creates every fst for all the different parameters of the testing phase.
### eval.py
Creates the file that will be passed to conlleval.
### eval.sh
Calls conlleval.pl for the evaluation, which is echoed in output.

## Results
In the same folder will be created many files:
1. All the FSTs created will be in the folder called "fsts"
  1.1 Except from train.fst, which will remain in src
2. The FAR, the CNTS and the LM files will be moved into "lm"
3. All the FSTs generated during the testing phase will be moved into the folder called "predicted"
4. The file prepared for the evaluation, made by eval.py, will be moved into "evaluations
5. At last, the final evaluation made with conlleval are moved into "output"
