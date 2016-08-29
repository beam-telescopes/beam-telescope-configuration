#!/bin/bash
# INPUTs
# which telescope
TELESCOPE='azalea'
# which sensors, at which positions
declare -a array=("chip101" "chip102" "chip103" "chip6b" "chip105" "chip69")

###########################################
TELESCOPE_PATH=$PWD
SENSOR_PATH=$PWD'/../../sensors/' 
SCRIPT_PATH=$PWD'/../../'

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
