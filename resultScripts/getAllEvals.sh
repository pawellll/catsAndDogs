cat results.dat | grep "Overall" | grep -o "0.[0-9]*$" > tmpOverall.dat
cat results.dat | grep -B 3 "Overall" | grep -o "Iter [0-9]*" | grep -o "[0-9]*" > iterTmp.dat
paste -d ' ' iterTmp.dat tmpOverall.dat > overall.dat
rm tmpOverall.dat
rm iterTmp.dat