method=$1

for i in `seq 1 5`;
do
    filename="eval_output_$i-$method.txt"
    ../P1_data/scripts/conlleval.pl < $filename
    echo ""
done