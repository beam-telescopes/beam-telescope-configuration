######################################
# Last update: 11 April 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "78"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 85
IVDREF1B = 189
IVDREF1C = 108
IVDREF1D = 111
# Thermal noise: TN
THN_matA = 1.031
THN_matB = 1.021
THN_matC = 1.013
THN_matD = 1.063
# Fixed pattern noise: FPN
FPN_matA = 0.5593
FPN_matB = 0.4468
FPN_matC = 0.6008
FPN_matD = 0.6711
# Offset
OFF_matA = 0.2581
OFF_matB = 0.3743
OFF_matC = 0.3418
OFF_matD = 0.3273
# columns to disable, if as a list 
DIS_col = []

######################################
# Generate using Jtag class
from generate_jtag import Jtag
# Constructor
chip = Jtag(sensor_name, IVDREF2, IVDREF1A, IVDREF1B, IVDREF1C, IVDREF1D, THN_matA, THN_matB, THN_matC, THN_matD, FPN_matA, FPN_matB, FPN_matC, FPN_matD, OFF_matA, OFF_matB, OFF_matC, OFF_matD, DIS_col)
# Print values
chip.values()
# Generate txt-files from threshold minimum to maximum
chip.generate(3, 12)

