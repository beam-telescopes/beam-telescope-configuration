ACONITE sensor setup
====================

SensorID (plane position) epi-layer and comments

Before Sept. 2015:
------------------
chip55 (0)  HR10
chip66 (1)  HR10
chip67 (2)  HR10
chip72b (3) HR10
chip69 (4)  HR15
chip81 (5)  HR20

September 2015:
---------------
* chip69 (4) chip69 shows high stand-by current 800mA instead of 350mA (incl. AUX board) --> ??
* chip81 (5) exchanged to have a homogenous HR10 telescope --> backup

January 2016:
-------------
chip55 (0) HR10
chip66 (1) HR10
chip67 (2) HR10
chip72 (3) HR10 (chip72b just renamed)
chip62 (4) HR10 (new)
chip59 (5) HR10 (new)

June 2016:
----------
observation at CERN / in ELab4, August 2016:
* chip67 (2) shows high stand-by current 700mA instead of 350mA (incl. AUX board) / confirmed plus fluctuating current between 600-940mA, "fluctuating picture", no stable clock/synchronization
* chip72 (3) shows plus 200mA in operation, 6 JTAG errors, parts of the sensor show no data / Matrix C is half-dead, Matrix D is dead = no output
* chip59 (5) high current, fluctuation / high current 0.8-1.2A, 1st JTAG is working, 2nd not plus unstable current

July 2016:
----------
Commissioning succesful: No JTAG errors, running current at 3.66A, data seems to be good:
chip55 (0) HR10
chip66 (1) HR10
chip81 (2) HR20 (new)
chip68 (3) HR20 (new)
chip62 (4) HR10
chip57 (5) HR10 (new)


October 2016:
------------
observation at CERN:
* chip55 (0) shows high current; stand-by 1.48A (incl. distr. boards) instead of ~350mA

Now, five plane telescope:
chip66 (0) HR10
chip81 (1) HR20 
chip68 (2) HR20 
chip62 (3) HR10
chip57 (4) HR10 

April/May 2017:
-----------
--> send chararcterized sensors to Andre Rummler: chip12b (AIDA), chip70
--> send broken sensors to Strassburg: chip 55, chip 59, chip 67, chip 72 --> see sensor report from 18.05.17

June 2017:
----------
chip70 (0) HR10 (new)
chip66 (1) HR10
chip81 (2) HR20 
chip68 (3) HR20
chip62 (4) HR10
chip57 (5) HR10

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
chip70  (0) HR10
chip18  (1) HR10 (new)
chip81  (2) HR20 
chip3   (3) HR10 (new)
chip9b  (4) HR10 (new)
chip10b (5) HR10 (new)
--> send new, chararcterized sensors to Andre Rummler



