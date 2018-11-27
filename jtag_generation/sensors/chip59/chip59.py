######################################
# Last update: 27 November 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "59"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 165
IVDREF1B = 150
IVDREF1C = 150
IVDREF1D = 123

# Thermal noise: TN
THN_matA = 0.9885
THN_matB = 1.015
THN_matC = 0.959
THN_matD = 0.9816

# Fixed pattern noise: FPN
FPN_matA = 0.3678
FPN_matB = 0.5103
FPN_matC = 0.6004
FPN_matD = 0.593

# Offset
OFF_matA = 0.2053
OFF_matB = -0.1815
OFF_matC = 0.1763
OFF_matD = 0.3448

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
