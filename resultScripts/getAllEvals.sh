result="/results.dat"
overall="/overall.dat"

cat $1$result | grep "Overall" | grep -o "0.[0-9]*$" > tmpOverall.dat
cat $1$result | grep "Overall" | grep -o "Iteration:[0-9]*" | grep -o "[0-9]*" > iterTmp.dat
paste -d ' ' iterTmp.dat tmpOverall.dat > $1$overall
rm tmpOverall.dat
rm iterTmp.dat