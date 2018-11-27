######################################
# Last update: 27 November 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "57"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 165
IVDREF1B = 145
IVDREF1C = 133
IVDREF1D = 208

# Thermal noise: TN
THN_matA = 1.001
THN_matB = 0.9518
THN_matC = 1.032
THN_matD = 0.9674

# Fixed pattern noise: FPN
FPN_matA = 0.4448
FPN_matB = 0.4832
FPN_matC = 0.5884
FPN_matD = 0.5446

# Offset
OFF_matA = -0.02545
OFF_matB = 0.3061
OFF_matC = -0.1391
OFF_matD = -0.36

# Disable columns/discriminators
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
