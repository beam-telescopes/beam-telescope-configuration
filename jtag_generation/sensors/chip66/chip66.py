######################################
# Last update: 27 November 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "66"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 190
IVDREF1B = 160
IVDREF1C = 201
IVDREF1D = 127
# Temporal noise: TN
THN_matA = 1.012
THN_matB = 0.9836
THN_matC = 1.055
THN_matD = 0.9287
# Fixed pattern noise: FPN
FPN_matA = 0.3518
FPN_matB = 0.4334
FPN_matC = 0.6135
FPN_matD = 0.5641
# Offset
OFF_matA = 0.1516
OFF_matB = 0.3196
OFF_matC = 0.0207
OFF_matD = 0.1993
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
