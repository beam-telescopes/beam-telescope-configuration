JTAG files generation for Mimosa26 sensors
==========================================
by Jan Dreyling-Eschweiler, 2015-1018

Overview / scripts:
-------------------
In ./scripts
* default_jtag.txt: for copying and adjusting register values
* generate_jtag.py: python-module for gnerating threshold files (txt) of one sensor
* adjust_position.sh: renaming threshold files due to telescope plane position
* generate_mcf.sh: generating master configuration file

Usage: generate JTAG-files for a sensor
---------------------------------------
* create a subfolder in sensors
* copy a chipX.py as template
* update values by the measured middlepoints, TNs, FPNs and offsets of all 4 matrices, and the columns, which should be disabled.
* python chipX.py creates threshold files 

Usgage: generate "telescope" configuration (mcf)
------------------------------------------------
* create a subfolder in telescopes
* copy a telescope.sh as template
* update names and order of chips
* source telescope.sh renames threshold files, save them in one folder, generates mcf


Version log:
------------
* Version 1: 4 Sep 2015
* Version 2: 15 Jan 2016
* Version 3: 23 Aug 2016, class Jtag
* Version 4: 09 Mar 2018, update Readme and scripts in dedicated folder



Some more details on jtag format and registers
==============================================

Adjust DAC values
-----------------
e.g. DAC-vlaues (XXX) of plane 0
* line 26: `XXX ; :BIAS_DAC[0][10] --> IVDREF1D`
* line 27: `XXX ; :BIAS_DAC[0][11] --> IVDREF1C`
* line 28: `XXX ; :BIAS_DAC[0][12] --> IVDREF1B`
* line 29: `XXX ; :BIAS_DAC[0][13] --> IVDREF1A`
* line 30: `XXX ; :BIAS_DAC[0][14] --> IVDREF2`

Change telescope plane
----------------------
Number in first []-brackets plus headers and trailers

Start signal
------------
Ext signal:
* Disable and set by JTAG: `0 ; :RO_MODE0[X][1]`
* Enable and set by clock: `1 ; :RO_MODE0[X][1]`

Setting:
* should be enabled
* however, for Artems integration, it doesn't matter
* but for the SBG integration, it is important!

Misc
----
IR[X]-parameter: 30, 25, 21, 15, 
--> No effect to performance of sensors

Test1Pad/Test2Pad
* Test1Pad: ClkDiv16 and Test2Pad: Calib
* `63 ; :CTRL_PIX[X][3]`

--> Test mode

* Test1Pad: Test_A and Test2Pad: Calib
* `7 ; :CTRL_PIX[X][3]`

--> ?

* Test1Pad: Test_A and Test2Pad: Test_D
* `0 ; :CTRL_PIX[X][3]`

--> operational mode

Deactivate columns, e.g. 1003:
* Enable (normal):     `0 ; :DIS_DISCRI[X][1003]`
* Disable (if broken): `1 ; :DIS_DISCRI[X][1003]`

Other
-----
diff files and remove ^M as end of line in unix files:
`tr -d '\r' <unix_file.txt | diff - win_file.txt`
