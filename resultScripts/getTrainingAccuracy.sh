cat results.dat | grep -o "Training Accuracy= 0.[0-9]*$" | grep -o "0.[0-9]*$" > tmpTrainingAccuracy.dat
cat results.dat | grep -o "Iter [0-9]*" | grep -o [0-9]* > iterTmp.dat
paste -d ' ' iterTmp.dat tmpTrainingAccuracy.dat > trainingAccuracy.dat
rm tmpTrainingAccuracy.dat
rm iterTmp.dat