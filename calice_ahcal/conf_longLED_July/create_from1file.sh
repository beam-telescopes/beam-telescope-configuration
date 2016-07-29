#!/bin/bash
COUNTERI=0
COUNTERJ=1

while [ $COUNTERI -lt 90 ]; 
do  
    CNT2DI=`seq -f "%02.0f" ${COUNTERI} ${COUNTERI}`
    echo "2digin counter I: ${CNT2DI}"
    CNT2DJ=`seq -f "%02.0f" ${COUNTERJ} ${COUNTERJ}`
    echo "2digin counter J: ${CNT2DJ}"
    /bin/cp -f $PWD/LED_$CNT2DI.conf $PWD/test.conf
    sed -i "s/LED_$CNT2DI/LED_$CNT2DJ/g" $PWD/test.conf
    /bin/cp -f $PWD/test.conf $PWD/LED_$CNT2DJ.conf
    let COUNTERI=COUNTERI+1
    let COUNTERJ=COUNTERJ+1
done

