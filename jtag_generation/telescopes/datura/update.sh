#!/bin/bash

# update DATURA jtag files 
# adjust extern start
# Jan Dreyling-Eschweiler
# 16 Sept 2015

# clear directory
rm -f jtag_datura/*.txt

# get current files
find 150913_config_files/ -name '*.txt' | parallel cp '{}' jtag_datura/

# remove current test files
cd jtag_datura/
rm *pad*
rm *ext*

# remove old plane5 files with wrong DAC value: BIAS_DAC[0][12] --> IVDREF1B
find ./ -not -name '*test*' -name 'pos5*' | parallel rm '{}'

# change name of correct plane5 files 
for files in *_test.txt; do 
mv -- "$files" "${files%_test.txt}.txt"
done

# difference of CTRL_8B10BREG1, IR ????
# B DAC value was manually adjusted by HJ using MimosaJTAG version ~1.7 ? on DATURA
#diff jtag_datura/pos0_chip73_thresh12.txt 150913_config_files/threshold12/pos0_chip73_thresh12.txt 
#diff jtag_datura/pos5_chip79_thresh12.txt 150913_config_files/threshold12/pos5_chip79_thresh12.txt

cd ..
