######################################
# Last update: 27 November 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "67"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 140
IVDREF1B = 110
IVDREF1C = 93
IVDREF1D = 143

# Thermal noise: TN
THN_matA = 1.031
THN_matB = 1.058
THN_matC = 1.105
THN_matD = 0.9633

# Fixed pattern noise: FPN
FPN_matA = 0.331
FPN_matB = 0.543
FPN_matC = 0.7585
FPN_matD = 0.623

# Offset
OFF_matA = 0.381
OFF_matB = 0.1134
OFF_matC = -0.2174
OFF_matD = 0.143

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
