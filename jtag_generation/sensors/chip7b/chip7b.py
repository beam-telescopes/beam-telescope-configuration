######################################
# Last update: 24 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "7b"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 118
IVDREF1B = 121
IVDREF1C = 145
IVDREF1D = 141
# Thermal noise: TN
THN_matA = 1.053
THN_matB = 1.008
THN_matC = 1.021
THN_matD = 0.9382
# Fixed pattern noise: FPN
FPN_matA = 0.4062
FPN_matB = 0.3832
FPN_matC = 0.5435
FPN_matD = 0.483
# Offset
OFF_matA = 0.5552
OFF_matB = 0.2977
OFF_matC = 0.2768
OFF_matD = 0.3896
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

