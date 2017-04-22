result="/results.dat"
loss="/loss.dat"

cat $1$result | grep -o "Minibatch Loss= [0-9]*.[0-9]*" | grep -o "[0-9]*.[0-9]*$" > tmpLoss.dat
cat $1$result | grep -o "Iter [0-9]*" | grep -o "[0-9]*" > iterTmp.dat

paste -d ' ' iterTmp.dat tmpLoss.dat > $1$loss
rm tmpLoss.dat
rm iterTmp.dat