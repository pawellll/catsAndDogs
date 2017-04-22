result="/results.dat"
iter="/iter.dat"

cat $1$result | grep -o "Iter [0-9]*" | grep -o "[0-9]*" > $1$iter