#!/bin/bash
# INPUTs
# which telescope
TELESCOPE='duranta_66'
# which sensors, at which positions
declare -a array=("chip2b" "chip5b" "chip107" "chip66" "chip7b" "chip3b")

###########################################
TELESCOPE_PATH=$PWD
SENSOR_PATH=$PWD'/../../sensors/' 
SCRIPT_PATH=$PWD'/../../scripts/'

rm jtag_$TELESCOPE/*.txt

# loop to create JTAG files with right position
arraylength=${#array[@]}
for (( i=0; i<${arraylength}; i++ ));
do
  echo $TELESCOPE "plane" $i ":" ${array[$i]}
  cd $SENSOR_PATH
  cd ${array[$i]}
  rm *.txt
  python ${array[$i]}.py
  cp $SCRIPT_PATH'adjust_position.sh' .
  source adjust_position.sh $i
  cp pos*.txt $TELESCOPE_PATH/jtag_$TELESCOPE
  rm adjust_position.sh
  cd $TELESCOPE_PATH
  # or do whatever with individual element of the array
done

# create master-configuration files i
WINFOLDER='C:\opt\jtag_'$TELESCOPE'\'
#cd $TELESCOPE_PATH
rm jtag_$TELESCOPE/*.mcf
echo $SCRIPT_PATH
cp $SCRIPT_PATH'generate_mcf.sh' .
source generate_mcf.sh $TELESCOPE $WINFOLDER
rm generate_mcf.sh 
#cd $TELESCOPE_PATH
