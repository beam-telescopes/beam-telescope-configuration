######################################
# Last update: 26 November 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "11b"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 140
IVDREF1B = 119
IVDREF1C = 139
IVDREF1D = 236

# Thermal noise: TN
THN_matA = 1.05
THN_matB = 0.6283
THN_matC = 1.009
THN_matD = 0.9398

# Fixed pattern noise: FPN
FPN_matA = 0.4373
FPN_matB = 0.3373
FPN_matC = 0.5933
FPN_matD = 0.5442

# Offset
OFF_matA = -0.1539
OFF_matB = 2.004
OFF_matC = -0.3311
OFF_matD = -0.03335

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
