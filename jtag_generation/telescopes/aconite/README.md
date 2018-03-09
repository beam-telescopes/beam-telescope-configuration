ACONITE sensor setup
====================

SensorID (plane position) epi-layer and comments

Before Sept. 2015:
------------------
0. chip55  HR10
1. chip66  HR10
2. chip67  HR10
3. chip72b HR10
4. chip69  HR15
5. chip81  HR20

September 2015:
---------------
* chip69 (4.) chip69 shows high stand-by current 800mA instead of 350mA (incl. AUX board) --> ??
* chip81 (5.) exchanged to have a homogenous HR10 telescope --> backup

January 2016:
-------------
0. chip55 HR10
1. chip66 HR10
2. chip67 HR10
3. chip72 HR10 (chip72b just renamed)
4. chip62 HR10 (new)
5. chip59 HR10 (new)

June 2016:
----------
observation at CERN / in ELab4, August 2016:
* chip67 (2.) shows high stand-by current 700mA instead of 350mA (incl. AUX board) / confirmed plus fluctuating current between 600-940mA, "fluctuating picture", no stable clock/synchronization
* chip72 (3.) shows plus 200mA in operation, 6 JTAG errors, parts of the sensor show no data / Matrix C is half-dead, Matrix D is dead = no output
* chip59 (5.) high current, fluctuation / high current 0.8-1.2A, 1st JTAG is working, 2nd not plus unstable current

July 2016:
----------
Commissioning succesful: No JTAG errors, running current at 3.66A, data seems to be good:
0. chip55 HR10
1. chip66 HR10
2. chip81 HR20 (new)
3. chip68 HR20 (new)
4. chip62 HR10
5. chip57 HR10 (new)


October 2016:
-------------
observation at CERN:
* chip55 (0.) shows high current; stand-by 1.48A (incl. distr. boards) instead of ~350mA

For intermediate, five plane telescope:
0. chip66 HR10
1. chip81 HR20 
2. chip68 HR20 
3. chip62 HR10
4. chip57 HR10 

April/May 2017:
---------------
--> send chararcterized sensors to Andre Rummler: chip12b (AIDA), chip70

--> send broken sensors to Strassburg: chip 55, chip 59, chip 67, chip 72 --> see sensor report from 18.05.17

June 2017:
----------
0. chip70 HR10 (new)
1. chip66 HR10
2. chip81 HR20 
3. chip68 HR20
4. chip62 HR10
5. chip57 HR10

December 2017/Feb. 2018:
------------------------
observation at CERN / in ELab4:
* chip 56 (AIDA 4): Matrix B hot
* chip 66 (1): 3 hot lines
* chip 68 (3): additional hot and dead column
* chip 62 (4): Matrix A dead 
* chip 57 (5): additional hot column

--> send these sensors to Strassburg --> see sensor report from 12.02.18

March 2018:
-----------
0. chip70  HR10
1. chip18  HR10 (new)
2. chip81  HR20 
3. chip3   HR10 (new)
4. chip9b  HR10 (new)
5. chip10b HR10 (new)

--> send new, chararcterized sensors to Andre Rummler
