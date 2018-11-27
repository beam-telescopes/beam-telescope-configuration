######################################
# Last update: 27 November 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "66"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 127
IVDREF1B = 115
IVDREF1C = 132
IVDREF1D = 94
# Temporal noise: TN
THN_matA = 1.037
THN_matB = 0.9707
THN_matC = 1.006
THN_matD = 0.9992
# Fixed pattern noise: FPN
FPN_matA = 0.4316
FPN_matB = 0.4338
FPN_matC = 0.484
FPN_matD = 0.5028
# Offset
OFF_matA = 0.2222
OFF_matB = 0.2318
OFF_matC = -0.1147
OFF_matD = 0.4469
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
