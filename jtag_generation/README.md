JTAG files generation for Mimosa26 sensors
==========================================


Ingredients:
- default_jtag.txt file
- python-script jtag_generator.py
- bash-script adjust_plane_position.sh

Generate JTAG-files (position 0)
--------------------------------

- Update jtag_generator.py using the measured middlepoints, TNs, FPNs and offsets of all 4 matrices, and the columns, which should be disabled.
- Execute: python jtag_generator.py

Change telescope plane
----------------------

- Choose a plane number (0 to 5)
- Execute: source adjust_plane_position.sh <number> 

Create master configuration file (mcf)
--------------------------------------

- adjust the variables TELESCOPE and WINFOLDER
- Execute: source mcf_generator.sh



JTAG files generation and manipulation
--------------------------------------

Ingredients:
- default_jtag.txt file
- python-script jtag_generator.py
- bash-script adjust_plane_position.sh

Generate JTAG-files (position 0)
--------------------------------

- Update jtag_generator.py using the measured middlepoints, TNs, FPNs and offsets of all 4 matrices.
- Execute: python jtag_generator.py

Change telescope plane
----------------------

- Choose a plane number (0 to 5)
- Execute: source adjust_plane_position.sh <number> 

ToDo
----
- Deactivate columns
- Creation of master configuration file (mcf)



by Jan Dreyling-Eschweiler, 4 Sep 2015









by Jan Dreyling-Eschweiler, 
Version 1: 4 Sep 2015
Version 2: 15 Jan 2016
Version 3: 23 Aug 2016, class Jtag





More information:

JTAG files generation and manipulation
--------------------------------------
by Jan Dreyling-Eschweiler, 4 Sep 2015
- creating class 23 Aug 2016


Ingredients:
- default_jtag.txt file
- python-script jtag_generator.py
- bash-script adjust_plane_position.sh

Generate JTAG-files (position 0)
--------------------------------

- Update jtag_generator.py using the measured middlepoints, TNs, FPNs and offsets of all 4 matrices.
- Execute: python jtag_generator.py

Adjust DAC values
-----------------
e.g. DAC-vlaues (XXX) of plane 0
line 26: XXX ; :BIAS_DAC[0][10] --> IVDREF1D
line 27: XXX ; :BIAS_DAC[0][11] --> IVDREF1C
line 28: XXX ; :BIAS_DAC[0][12] --> IVDREF1B
line 29: XXX ; :BIAS_DAC[0][13] --> IVDREF1A
line 30: XXX ; :BIAS_DAC[0][14] --> IVDREF2


Change telescope plane
----------------------
(Number in first []-brackets plus headers and trailers)

- Choose a plane number (0 to 5)
- Execute: source adjust_plane_position.sh <number> 

Start signal
------------
Ext signal:
Disable and set by JTAG: 0 ; :RO_MODE0[X][1]
Enable and set by clock: 1 ; :RO_MODE0[X][1]
--> should be enabled
(For Artems integration, it doesn't matter. But for the SBG integration, it is important!)


More
----
- IR[X]-parameter: 30, 25, 21, 15, 
--> No effect to performance of sensors

- Test1Pad/Test2Pad
Test1Pad: ClkDiv16
Test2Pad: Calib
63 ; :CTRL_PIX[X][3]
--> Test mode

Test1Pad: Test_A
Test2Pad: Calib
7 ; :CTRL_PIX[X][3] 

Test1Pad: Test_A
Test2Pad: Test_D
0 ; :CTRL_PIX[X][3]
--> operational mode

- Deactivate columns, e.g. 1003:
Enable (normal):     0 ; :DIS_DISCRI[X][1003]
Disable (if broken): 1 ; :DIS_DISCRI[X][1003]

- Creation of master configuration file (mcf):
mcf_generator.sh

- diff files and remove ^M as end of line in unix files:
tr -d '\r' <unix_file.txt | diff - win_file.txt









