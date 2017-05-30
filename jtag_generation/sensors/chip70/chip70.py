######################################
# Last update: 29 May 2017, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "70"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 102
IVDREF1B = 130
IVDREF1C = 150
IVDREF1D = 172
# Thermal noise: TN
THN_matA = 1.047
THN_matB = 1.043
THN_matC = 0.9951
THN_matD = 1.052
# Fixed pattern noise: FPN
FPN_matA = 0.3811
FPN_matB = 0.525
FPN_matC = 0.6516
FPN_matD = 0.6336
# Offset
OFF_matA = 0.1688
OFF_matB = -0.09585
OFF_matC = 0.1234
OFF_matD = -0.2837
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

