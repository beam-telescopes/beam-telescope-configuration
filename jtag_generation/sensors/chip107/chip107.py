######################################
# Last update: 24 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "107"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 143
IVDREF1B = 68
IVDREF1C = 133
IVDREF1D = 102
# Thermal noise: TN
THN_matA = 0.9302
THN_matB = 0.8972
THN_matC = 0.9157
THN_matD = 0.8811
# Fixed pattern noise: FPN
FPN_matA = 0.4848
FPN_matB = 0.4291
FPN_matC = 0.5477
FPN_matD = 0.4041
# Offset
OFF_matA = -0.1321
OFF_matB = -0.1535
OFF_matC = -0.09622
OFF_matD = 0.02095
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

