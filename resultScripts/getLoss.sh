cat results.dat | grep -o "Minibatch Loss= [0-9]*.[0-9]*" | grep -o "[0-9]*.[0-9]*$" > tmpLoss.dat
cat results.dat | grep -o "Iter [0-9]*" | grep -o [0-9]* > iterTmp.dat
paste -d ' ' iterTmp.dat tmpLoss.dat > loss.dat
rm tmpLoss.dat
rm iterTmp.dat