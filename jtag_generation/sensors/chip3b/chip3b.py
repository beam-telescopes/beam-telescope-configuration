######################################
# Last update: 24 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "3b"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 110
IVDREF1B = 153
IVDREF1C = 124
IVDREF1D = 143
# Thermal noise: TN
THN_matA = 0.9655
THN_matB = 0.9486
THN_matC = 0.9411
THN_matD = 0.8953
# Fixed pattern noise: FPN
FPN_matA = 0.4482
FPN_matB = 0.441
FPN_matC = 0.5132
FPN_matD = 0.5393
# Offset
OFF_matA = 0.3885
OFF_matB = 0.2727
OFF_matC = 0.4043
OFF_matD = 0.7676
# columns to disable, if as a list 
DIS_col = [1003]

######################################
# Generate using Jtag class
from generate_jtag import Jtag
# Constructor
chip = Jtag(sensor_name, IVDREF2, IVDREF1A, IVDREF1B, IVDREF1C, IVDREF1D, THN_matA, THN_matB, THN_matC, THN_matD, FPN_matA, FPN_matB, FPN_matC, FPN_matD, OFF_matA, OFF_matB, OFF_matC, OFF_matD, DIS_col)
# Print values
chip.values()
# Generate txt-files from threshold minimum to maximum
chip.generate(3, 12)

