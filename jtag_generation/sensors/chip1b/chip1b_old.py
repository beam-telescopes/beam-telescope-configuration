######################################
# Last update: 24 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "1b"

# Middlepoints in DAC
IVDREF2  = 98
IVDREF1A = 127
IVDREF1B = 116
IVDREF1C = 130
IVDREF1D = 93
# Temporal noise: TN
THN_matA = 0.9723 
THN_matB = 0.9145
THN_matC = 0.9700
THN_matD = 0.9181
# Fixed pattern noise: FPN
FPN_matA = 0.4271
FPN_matB = 0.4548
FPN_matC = 0.4744
FPN_matD = 0.496
# Offset
OFF_matA = 0.5116
OFF_matB = 0.2303
OFF_matC = 0.529
OFF_matD = 0.6422
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
