######################################
# Last update: 02 May 2017, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "12b"

# Middlepoints in DAC
IVDREF2  = 98 
IVDREF1A = 69
IVDREF1B = 117
IVDREF1C = 147
IVDREF1D = 125
# Thermal noise: TN
THN_matA = 1.02
THN_matB = 0.9995
THN_matC = 0.9657
THN_matD = 0.994
# Fixed pattern noise: FPN
FPN_matA = 0.465
FPN_matB = 0.5244
FPN_matC = 0.5885
FPN_matD = 0.6201
# Offset
OFF_matA = 0.04006
OFF_matB = 0.06652
OFF_matC = -0.08167
OFF_matD = -0.2759
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

