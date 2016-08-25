######################################
# Last update: 25 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "102"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 138
IVDREF1B = 138
IVDREF1C = 153
IVDREF1D = 111

# Thermal noise: TN
THN_matA = 1.004
THN_matB = 0.9473
THN_matC = 0.9499
THN_matD = 0.9216

# Fixed pattern noise: FPN
FPN_matA = 0.4528
FPN_matB = 0.4707
FPN_matC = 0.502
FPN_matD = 0.4794

# Offset
OFF_matA = -0.006314
OFF_matB = 0.06399
OFF_matC = 0.000163
OFF_matD = 0.06878

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
