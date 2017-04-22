trainingAccuracy="/trainingAccuracy.dat"
results="/results.dat"

cat $1$results | grep -o "Training Accuracy= 0.[0-9]*$" | grep -o "0.[0-9]*$" > tmpTrainingAccuracy.dat
cat $1$results | grep -o "Iter [0-9]*" | grep -o "[0-9]*" > iterTmp.dat

paste -d ' ' iterTmp.dat tmpTrainingAccuracy.dat > $1$trainingAccuracy
rm tmpTrainingAccuracy.dat
rm iterTmp.dat