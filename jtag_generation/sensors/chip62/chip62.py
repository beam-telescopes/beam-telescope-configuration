######################################
# Last update: 25 August 2016, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "62"

# Middlepoints in DAC
IVDREF2  = 100 
IVDREF1A = 117
IVDREF1B = 143
IVDREF1C = 175
IVDREF1D = 127

# Thermal noise: TN
THN_matA = 0.9896
THN_matB = 0.9135
THN_matC = 0.9652
THN_matD = 0.9183

# Fixed pattern noise: FPN
FPN_matA = 0.3488
FPN_matB = 0.3527
FPN_matC = 0.5697
FPN_matD = 0.511

# Offset
OFF_matA = -0.1569
OFF_matB = 0.0030
OFF_matC = -0.1777
OFF_matD = 0.1453

# Disable columns/discriminators
DIS_col = [843]

######################################
# Generate using Jtag class
from generate_jtag import Jtag
# Constructor
chip = Jtag(sensor_name, IVDREF2, IVDREF1A, IVDREF1B, IVDREF1C, IVDREF1D, THN_matA, THN_matB, THN_matC, THN_matD, FPN_matA, FPN_matB, FPN_matC, FPN_matD, OFF_matA, OFF_matB, OFF_matC, OFF_matD, DIS_col)
# Print values
chip.values()
# Generate txt-files from threshold minimum to maximum
chip.generate(3, 12)
