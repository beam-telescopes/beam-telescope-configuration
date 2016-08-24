######################################
# Last update: 24 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "2b"

# Middlepoints in DAC
IVDREF2  = 102 
IVDREF1A = 129
IVDREF1B = 38
IVDREF1C = 82
IVDREF1D = 96
# Thermal noise: TN
THN_matA = 0.9883 
THN_matB = 1.002
THN_matC = 0.9812
THN_matD = 0.9835
# Fixed pattern noise: FPN
FPN_matA = 0.4422
FPN_matB = 0.4709
FPN_matC = 0.4918
FPN_matD = 0.519
# Offset
OFF_matA = 0.3474
OFF_matB = 0.3906
OFF_matC = 0.3812
OFF_matD = 0.6523
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
