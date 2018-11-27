######################################
# Last update: 27 November 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "68"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 148
IVDREF1B = 146
IVDREF1C = 171
IVDREF1D = 163

# Thermal noise: TN
THN_matA = 1.033
THN_matB = 0.9657
THN_matC = 0.9153
THN_matD = 0.8995

# Fixed pattern noise: FPN
FPN_matA = 0.5624
FPN_matB = 0.5109
FPN_matC = 0.5419
FPN_matD = 0.551

# Offset
OFF_matA = -0.1598
OFF_matB = 0.0928
OFF_matC = 0.07012
OFF_matD = -0.4875

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
