######################################
# Last update: 08 March 2018, Jan Dreyling-Eschweiler

######################################
# Sensor Name
sensor_name = "10b"

# Middlepoints in DAC
IVDREF2  = 100
IVDREF1A = 150
IVDREF1B = 145
IVDREF1C = 121
IVDREF1D = 210

# Thermal noise: TN
THN_matA = 1.093
THN_matB = 0.9535
THN_matC = 1.016
THN_matD = 1.006

# Fixed pattern noise: FPN
FPN_matA = 0.4204
FPN_matB = 0.5108
FPN_matC = 0.7331
FPN_matD = 0.6334

# Offset
OFF_matA = 0.1073
OFF_matB = -0.1837
OFF_matC = -0.1247
OFF_matD = -0.1453

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
