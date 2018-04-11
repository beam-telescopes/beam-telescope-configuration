#!/bin/bash
# update DATURA jtag files 
# Jan Dreyling-Eschweiler, 11 April 2018

TELESCOPE='datura'
TELESCOPE_PATH=$PWD
SENSOR_PATH=$PWD'/../../sensors/' 
SCRIPT_PATH=$PWD'/../../scripts/'

# rename old files
# clear directory
rm -f jtag_$TELESCOPE/*.txt
# get current files
find 150913_jtag_files/ -name '*.txt' | parallel cp '{}' jtag_$TELESCOPE
# remove current test files
cd $TELESCOPE_PATH/jtag_$TELESCOPE
rm *pad*
rm *ext*

# new plane 3 --> chip78
cd $TELESCOPE_PATH/jtag_$TELESCOPE
# clean
rm pos3*.txt
# create jtag files
cd $SENSOR_PATH/chip78
rm *.txt
python chip78.py
# rename pos
cp $SCRIPT_PATH'adjust_position.sh' .
source adjust_position.sh 3
cp pos*.txt $TELESCOPE_PATH/jtag_$TELESCOPE
rm adjust_position.sh

# remove old plane5 files with wrong DAC value: BIAS_DAC[0][12] --> IVDREF1B
cd $TELESCOPE_PATH/jtag_$TELESCOPE
find ./ -not -name '*test*' -name 'pos5*' | parallel rm '{}'
# change name of correct plane5 files 
for files in *_test.txt; do 
mv -- "$files" "${files%_test.txt}.txt"
done
# DAC value was manually corrected by HJ using MimosaJTAG on DATURA
#diff jtag_datura/pos0_chip73_thresh12.txt 150913_config_files/threshold12/pos0_chip73_thresh12.txt 
#diff jtag_datura/pos5_chip79_thresh12.txt 150913_config_files/threshold12/pos5_chip79_thresh12.txt

# adjust register
cd $TELESCOPE_PATH/jtag_$TELESCOPE
cp $SCRIPT_PATH'adjust_register.sh' .
source adjust_register.sh
rm adjust_register.sh

# adjust extern start
# 0 ; :RO_MODE0[X][1] --> 1 ; :RO_MODE0[X][1]
# adjust ctrl_pix
# 63 ; :CTRL_PIX[X][3] --> 0 ; :CTRL_PIX[X][3]

# create master-configuration files i
cd $TELESCOPE_PATH
WINFOLDER='C:\opt\jtag_'$TELESCOPE'\'
#cd $TELESCOPE_PATH
rm jtag_$TELESCOPE/*.mcf
echo $SCRIPT_PATH
cp $SCRIPT_PATH'generate_mcf.sh' .
source generate_mcf.sh $TELESCOPE $WINFOLDER
rm generate_mcf.sh 
cd $TELESCOPE_PATH
