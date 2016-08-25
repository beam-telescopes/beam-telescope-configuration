#!/bin/bash

# generates mcf files
# Jan Dreyling-Eschweiler
# 16 Sept 2015


TELESCOPE='duranta'
WINFOLDER='C:\opt\jtag_'$TELESCOPE'\'
DESTINATION='./jtag_'$TELESCOPE'/'
THRESHOLDS=(thresh3 thresh4 thresh5 thresh6 thresh7 thresh8 thresh9 thresh10 thresh11 thresh12) 
NOW=$(date +"%m-%d-%Y")

cd $DESTINATION
rm *.mcf
cd ..


# change name of correct plane5 files 
for threshold in "thresh3" "thresh4" "thresh5" "thresh6" "thresh7" "thresh8" "thresh9" "thresh10" "thresh11" "thresh12"; do 

# create file
FILE=$DESTINATION$threshold"_"$TELESCOPE".mcf"
echo $FILE
touch $FILE

# start lines
echo "#JTAG_MS MASTER CONFIGURATION FILE "$NOW >> $FILE
echo "6 ; number of devices" >> $FILE

# position loop
for position in "0" "1" "2" "3" "4" "5"; do
cd $DESTINATION
JTAGFILE="pos"$position"*"$threshold"*"
JTAGFILE=$(ls -1 $JTAGFILE)
cd ..
echo $WINFOLDER$JTAGFILE  "   ; ("$position")" >> $FILE 
done

# end lines
echo "#END OF JTAG_MS MASTER CONFIGURATION FILE" >> $FILE
echo 

done

