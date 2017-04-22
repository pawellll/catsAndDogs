bash getAllEvals.sh $1
bash getLoss.sh $1
bash getTrainingAccuracy.sh $1

gunplot="gnuplot.gpl"

cp gnuplot.gpl $1
cd $1
gnuplot $gunplot
rm $gunplot
