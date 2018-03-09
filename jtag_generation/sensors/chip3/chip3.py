######################################
# Last update: 08 March 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "3"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 144
IVDREF1B = 171
IVDREF1C = 132
IVDREF1D = 88

# Thermal noise: TN
THN_matA = 1.016
THN_matB = 1.026
THN_matC = 0.9764
THN_matD = 0.9658

# Fixed pattern noise: FPN
FPN_matA = 0.4772
FPN_matB = 0.5384
FPN_matC = 0.6084
FPN_matD = 0.5991

# Offset
OFF_matA = 0.008371
OFF_matB = -0.2582
OFF_matC = -0.6084
OFF_matD = -0.1458

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
