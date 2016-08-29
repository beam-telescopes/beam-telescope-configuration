######################################
# Last update: 24 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "1b"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 127
IVDREF1B = 117
IVDREF1C = 132
IVDREF1D = 95
# Temporal noise: TN
THN_matA = 0.9971 
THN_matB = 0.934
THN_matC = 0.9765
THN_matD = 0.9339
# Fixed pattern noise: FPN
FPN_matA = 0.3689
FPN_matB = 0.3718
FPN_matC = 0.4705
FPN_matD = 0.4247
# Offset
OFF_matA = 0.5314
OFF_matB = 0.2413
OFF_matC = 0.4318
OFF_matD = 0.5257
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
