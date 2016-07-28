#!/bin/bash
COUNTERI=0
COUNTERJ=1

while [ $COUNTERI -lt 5 ]; 
do  
    /bin/cp -f $PWD/LED_0$COUNTERI.conf $PWD/test.conf
    sed -i "s/LED_0$COUNTERI/LED_0$COUNTERJ/g" $PWD/test.conf
    if [ $COUNTERI -eq 4 ]
    then
	sed -i "s/NextConfigFileOnFileLimit/\#NextConfigFileOnFileLimit/g" $PWD/test.conf
    fi
    /bin/cp -f $PWD/test.conf $PWD/LED_0$COUNTERJ.conf
    let COUNTERI=COUNTERI+1
    let COUNTERJ=COUNTERJ+1
done

rm $PWD/test.conf
