######################################
# Last update: 08 March 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "9b"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 142
IVDREF1B = 86
IVDREF1C = 144
IVDREF1D = 127

# Thermal noise: TN
THN_matA = 1.022
THN_matB = 1.016
THN_matC = 0.987
THN_matD = 0.9204

# Fixed pattern noise: FPN
FPN_matA = 0.5197
FPN_matB = 0.5604
FPN_matC = 0.6137
FPN_matD = 0.6027

# Offset
OFF_matA = -0.07018
OFF_matB = -0.1056
OFF_matC = -0.1717
OFF_matD = -0.2145

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
